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


def shorten_filenames():
    download_folder = "./input/corrupted/"
    max_length = 190  # Max length for Windows file paths is 260 characters

    for filename in os.listdir(download_folder):
        if filename.endswith(".pdf"):
            file_path = os.path.join(download_folder, filename)
            if len(filename) > max_length:
                new_filename = filename[:max_length] + ".pdf"
                new_file_path = os.path.join(download_folder, new_filename)
                os.rename(file_path, new_file_path)
                print(f"Renamed {filename} to {new_filename}")
