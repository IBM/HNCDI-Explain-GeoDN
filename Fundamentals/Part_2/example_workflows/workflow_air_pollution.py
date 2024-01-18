# Copyright (c) 2024 International Business Machines Corporation

# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

# Written by Junaid Butt <junaid.butt@ibm.com> and Geoffery Dawson <Geoffrey.Dawson@ibm.com>

def main(payload, prefix: str):
    from geodn.modeling.component import component_from_text, Component
    import json

    ####-------------------------------------------------------------
    #    Import workflow components
    ####-------------------------------------------------------------
    
    data_inject = component_from_text(
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
            - tif*
            - csv
      secrets:
        - name: COSCRED
    """
    )

    air_pollution = component_from_text(
        """
    image: us.icr.io/geodn/air-pollution-time-series:latest
    name: air-pollution-time-series
    operations:
        command:
            - python
            - fit_ts_model.py
        inputs:
            - containerPath: /
              file:
                - warrington_2020_daily_mean_pm10.csv
        outputs:
            - containerPath: /model_assets/model_output/
              file:
                - warrington_pm10_daily_forecast_plot.png
                - warrington_pm10_daily_forecast.csv
            - containerPath: /model_assets/models/
              file:
                - warrington_pm10_daily_forecast_model.np
    """
    )

    ####-------------------------------------------------------------
    #    Construct workflow input/config files - e.g. PAIRS query specifications
    ####-------------------------------------------------------------


    inputFiles = [
        {
            "filename": "injectionfile.json",
            "content": json.dumps( [payload['workflow_options']['input_data'][X] for X in list(payload['workflow_options']['input_data'].keys())  ]),
            "prefix": prefix
        }
    ]

    ####-------------------------------------------------------------
    #    Construct the workflow DAG
    ####-------------------------------------------------------------

    dag: list[Component] = []

    dag.append(
        data_inject.new()
        .params(queryconfigpath="injectionfile.json")
        .name("data-inject")
        .prefix(prefix)
        .secrets_from_kubernetes("coscred")
        .env_vars(
            {
                "INJECTFILE": "injectionfile.json"
            }
        )
    )

    # Air Pollution component.
    dag.append(
        air_pollution.new()
        .name("air-pollution-time-series")
        .parents("data-inject")
        .env_vars({"LOGLEVEL": "DEBUG"})
        .retry(1)
    )

    return  (dag, inputFiles)