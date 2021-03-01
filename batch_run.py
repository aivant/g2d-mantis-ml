import glob
import subprocess

import pandas as pd


def _get_diseases(config_path="mantis_ml/conf/", output_path="out/"):
    """
    Returns a list of files that end with yaml in
    the specified directory

    Files should be named in the format disease_config.yaml
    for this to work
    """
    config_file_list = glob.glob(config_path + "*.yaml")
    output_folder_list = [
        (output_path + file.split("/")[2].split("_")[0]) for file in config_file_list
    ]
    return list(zip(config_file_list, output_folder_list))


def run_mantis(zipped_paths, thread_count="12"):
    """
    Runs the mantis call associated with the disease and path
    will take a long time....

    Example function call to mantis:
    mantisml -c mantis_ml/conf/Epilepsy_config.yaml -o out/Epilepsy-test -n 12
    """
    process_status_list = []
    for disease in zipped_paths:
        # try:
        function_call = [
            "mantisml",
            "-c",
            disease[0],
            "-o",
            disease[1],
            "-n",
            thread_count,
        ]
        try:
            subprocess.run(function_call, stdout=subprocess.DEVNULL)
            process_status_list.append([disease[0], disease[1], "success"])
        except:
            process_status_list.append([disease[0], disease[1], "failure"])
    process_success = pd.DataFrame(
        columns=["config_path", "output_path", "status"], data=process_status_list
    )
    return process_success


if __name__ == "__main__":
    """
    Modify this if you want different input, output, etc
    """
    zipped_paths = _get_diseases()
    status = run_mantis(zipped_paths)
    status.to_csv("batch_run_status.csv", index=False)
