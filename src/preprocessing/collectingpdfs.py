import os

import requests


def collect_pdfs():
    api_url = "https://api.github.com/repos/tpn/pdfs/contents"
    download_folder = "./input/pdfs/"

    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    response = requests.get(api_url)
    if response.status_code == 200:
        repo_contents = response.json()
        for item in repo_contents:
            if item["download_url"] and item["download_url"].endswith(".pdf"):
                pdf_url = item["download_url"]
                pdf_name = pdf_url.split("/")[-1]
                pdf_path = os.path.join(download_folder, pdf_name)

                print(f"Downloading {pdf_name}...")
                pdf_response = requests.get(pdf_url)
                with open(pdf_path, "wb") as pdf_file:
                    pdf_file.write(pdf_response.content)
                print(f"{pdf_name} downloaded and saved to {pdf_path}.")
    else:
        print(
            f"Failed to retrieve repository contents. Status code: {response.status_code}"
        )
