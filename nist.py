import requests
import json
import datetime

from requests import api

software_name = "Microsoft"
start_days = 20 # Max range is 120 consecutive days.
severity = "HIGH"
url = "https://services.nvd.nist.gov/rest/json/cves/2.0"


def get_vulnerabilities():
    pubEndDate = datetime.datetime.now().isoformat()
    pubStartDate = (datetime.datetime.now() - datetime.timedelta(days=start_days)).isoformat()

    api_url = f"{url}?keywordSearch={software_name}&cvssV3Severity={severity}&pubStartDate={pubStartDate}&pubEndDate={pubEndDate}"
    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            return json.loads(response.text)["vulnerabilities"]
        else:
            exit(f"[Error] {response}")
    except Exception as exception:
        exit(f"[Error] {exception} {response.text}")


def main():
    vulnerabilities = get_vulnerabilities()
    print(f"[Info] {len(vulnerabilities)} reported vulnerabilities")

    # for cve_item in vulnerabilities:
    #     cve_id = cve_item["cve"]["CVE_data_meta"]["ID"]
    #     print(cve_id)

    # Store in Azure DB
    # Connect to Flask on Azure


if __name__ == "__main__":
    main()
