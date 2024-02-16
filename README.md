# Bulk distance calculator
Simple Python script that calculates road distance in bulk, for a list of origins and destinations.

## How it works
The script reads from a tab separated input file and save the results in a tab separated output file. The names of the files can be set in the script as `inputfile` and `outputfile`.

The input file is a tab separated file that can contain any number of columns, but it should contain at least 3 mandatory columns (in any position):

- *Unique id* - a field used for matching the output with the input. It's position should be set in the variable `idx_uniq_id` in the script. Please note that position start with 0 instead of 1, for the first column.
- *Origin* - can be either full addresses (eg:Eiffel Tower, Paris, France) or comma separated gps coordinates (eg: 51.5031897,-0.1220941). It's position should be set in the variable `idx_origin` in the script.
- *Destination* - can be either full addresses (eg:Eiffel Tower, Paris, France) or comma separated gps coordinates (eg: 51.5031897,-0.1220941). It's position should be set in the variable `idx_destination` in the script.

The script retrieves the data from Google Maps API, so a [Google Maps API key](https://developers.google.com/maps/documentation/javascript/get-api-key) is required. You should enter it between the quotes as the variable `key`.

## Credits
The script was inspired by this [Harward University script](https://gis.harvard.edu/batch-distance-calculation-using-google-distance-matrix-api).
