# Smart VIN Decoder

A solo Information Systems semester project by Sam Miller: a Python command-line application that looks up vehicle information through the NHTSA vPIC API. Built to practice API integration, JSON parsing, input checks, and organizing data in a menu-driven application.

## What it does

- Accepts a VIN and requests vehicle details from the NHTSA API.
- Displays available make, model, year, manufacturer, engine, fuel, vehicle type, and plant information.
- Keeps VINs and their makes in memory during the current session.
- Lets you revisit a lookup or delete a history entry after confirmation.
- Checks input length, alphanumeric characters, and the presence of both letters and numbers before requesting data.

## Run locally

Requires Python 3 and an internet connection. The only third-party Python dependency is `requests`.

```sh
git clone https://github.com/ksu-is/Smart-VIN-Decoder.git
cd Smart-VIN-Decoder
python -m venv .venv
```

Activate the environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Or on macOS / Linux:

```sh
source .venv/bin/activate
```

Then install the dependency and start the application:

```sh
python -m pip install requests
python vin_decoder.py
```

On systems where Python 3 is named `python3`, use that command when creating the environment.

## Example session

Enter a name, choose **1) Decode a VIN**, and enter a 17-character VIN. For example, `1HGCM82633A004352` can be used as a sample lookup. The application displays fields returned by NHTSA; blank fields are shown as `UNAVAILABLE`.

The menu provides:

```text
1) Decode a VIN
2) View Decoded VIN History
3) Delete a VIN from History
4) Exit
```

Choose **2** to view session history. Selecting an entry requests its details from the API again. Choose **3** to remove an entry, or enter `back` when prompted to return to the menu.

## Implementation

`vin_decoder.py` contains the application:

- `is_valid_vin()` performs basic input checks.
- `decode_vin()` makes the HTTP request, parses JSON, displays fields, and updates history.
- `input_history()` lists history and allows a fresh request for a selected VIN.
- `delete_vin()` handles selection and deletion confirmation.
- `main()` runs the interactive menu.

I implemented the Python application as a solo project for my Information Systems course. The [project roadmap](projectroadmap.md) records the coursework milestones. The [semester presentation](SMART%20VIN%20DECODER%20PRESENTATION.pptx) is also included.

## Current limitations

- History is stored in memory and is lost when the application closes.
- History stores the VIN and make, rather than a cached full API response.
- The input checks do not validate a VIN check digit or every VIN-specific character rule.
- Non-200 HTTP responses and empty core vehicle fields have basic messages. Request timeouts, connection exceptions, and unexpected JSON structures are not comprehensively handled.
- API results depend on the data available from NHTSA. This is a coursework tool, not an authoritative vehicle-history service.

## References and license

- [NHTSA vPIC API](https://vpic.nhtsa.dot.gov/api/): vehicle data source.
- [vininfo](https://github.com/idlesign/vininfo) and [pyvin](https://github.com/arpuffer/pyvin): references recorded in the original project documentation; neither is required to run this application.

Licensed under the [MIT License](LICENSE).
