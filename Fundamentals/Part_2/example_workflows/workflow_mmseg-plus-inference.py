# Copyright (c) 2024 International Business Machines Corporation

# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

def main(payload, prefix: str):
    import json
    from geodn.modeling.component import component_from_text, Component
    from geoft.geoft_utils import generate_config
    
    
    mmseg_data_inject = component_from_text(
        """
    image: us.icr.io/cimf-modules/cimf-data-injector:latest
    name: cimf-data-injector
    operations:
      command:
        - python
        - data_injector.py
      inputs:
        - containerPath: /
          file:
            - injectionfile.json
      outputs:
        - containerPath: /
          fileSuffix:
            - tif
            - py
            - yaml
            - pt
            - csv
      secrets:
        - name: COSCRED
    """
    )
    
    mmseg_burn_scar = component_from_text(
        """
    image: us.icr.io/geodn/mmsegmentation:latest
    name: mmseg-burn-scars
    operations:
        args:
            - $(burn_scars_template)
        command:
            - python
            - tools/train.py
        inputs:
            - containerPath: /mmsegmentation/
              fileSuffix:
                - py
                - yaml
                - pt
                - csv
            - containerPath: /mmsegmentation/
              file:
                - $(burn_scars_template)
            - containerPath: /mmsegmentation/training
              fileSuffix:
                - train_merged.tif
                - train.mask.tif
            - containerPath: /mmsegmentation/testing
              fileSuffix:
                - val_merged.tif
                - val.mask.tif
        outputs:
            - containerPath: /mmsegmentation/
              fileSuffix:
                - tif
                - csv
                - pt
                - json
                - pth
                - py
    """
    )

    mmseg_burn_scar_infer = component_from_text(
        """
    image: us.icr.io/geodn/mmsegmentation:latest
    name: mmseg-burn-scars-infer
    operations:
        args:
            - '-config'
            - $(burn_scars_template)
            - '-ckpt'
            - $(ckpt)
            - '-input'
            - $(input)
            - '-output'
            - $(output)
            - '-bands'
            - $(bands)
                
        command:
            - python
            - tools/geospatial_batch_inference_explain_c3.py

        inputs:
            - containerPath: /mmsegmentation/
              fileSuffix:
                - py
                - yaml
                - pt
                - csv
                - pth
            - containerPath: /mmsegmentation/
              file:
                - $(burn_scars_template)
            - containerPath: /mmsegmentation/inference
              fileSuffix:
                - inf_merged.tif
        outputs:
            - containerPath: /mmsegmentation/
              fileSuffix:
                - tif
                - csv
                - pt
                - json
                - pth
                - py
            - containerPath: /mmsegmentation/inference
              fileSuffix:
                - tif               
    """
    )

    config_file_name = "burn_scars_hf_template.py"
    experiment_name, experiment_filepath = generate_config(
        payload['workflow_options']["model_options"]["project_name"],
        payload['workflow_options']["model_options"],
        "example_workflows/burn_confg_hf.py.template"
        )

    with open(experiment_filepath) as file:
        burn_template_string = file.read()

    def python_dumps(filename: str, file_contents_as_string: str) -> None:       
        with open(filename, 'w') as f:
            f.write(file_contents_as_string)


    inputFiles = [
                {
                    "filename": "injectionfile.json",
                    "content": json.dumps([payload['workflow_options']['input_data'][X] for X in list(payload['workflow_options']['input_data'].keys())]),
                    "prefix": prefix
                },
                {
                    "filename": config_file_name,
                    "content": burn_template_string,
                    "prefix": prefix
                },
            ]

    ####-------------------------------------------------------------
    #    Construct the workflow DAG
    ####-------------------------------------------------------------

    dag: list[Component] = []


    # Inject  data.
    dag.append(
        mmseg_data_inject.new()
        .params(queryconfigpath="injectionfile.json")
        .name("mmseg-data-injection")
        .prefix(prefix)
        .secrets_from_kubernetes("coscred")
        .env_vars(
            {
                "INJECTFILE": "injectionfile.json"
            }
            )
    )

    # MMseg Burn Scars
    dag.append(
        mmseg_burn_scar.new()
        .params(burn_scars_template=config_file_name)
        .name("fine-tune-model")
        .prefix(prefix)
        .parents("mmseg-data-injection")
        .timeout("4320m")
        .resources(
            {
                "cpu": payload["workflow_options"]["cpu"],
                "memory": payload["workflow_options"]["memory"],
                "nvidia.com/gpu": payload["workflow_options"]["gpu"],
            }
        )
    )    

                
    # MMseg Burn Scars
    dag.append(
        mmseg_burn_scar_infer.new()
        .params(burn_scars_template=config_file_name,
                ckpt = 'None',
                input = 'inference/',
                output = 'inference/',
                bands = '[0,1,2,3,4,5]' ,
                )
        .name("fine-tune-model-infer")
        .prefix(prefix)
        .parents("fine-tune-model")
        .resources(
            {
                "cpu": payload["workflow_options"]["cpu"],
                "memory": payload["workflow_options"]["memory"],
                "nvidia.com/gpu": payload["workflow_options"]["gpu"],
            }
        )
    )        
  
    ####-------------------------------------------------------------
    #    Compile the workflow to tekton wf definition
    ####-------------------------------------------------------------

    # workflow = kfp_tekton.KFPTektonCompiler("ifm-standard", dag)
    return (
        dag,
        inputFiles
    )

