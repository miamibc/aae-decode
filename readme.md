# AAE Decode Utility

This project provides a Python utility to decode [Apple's AAE](http://fileformats.archiveteam.org/wiki/AAE_sidecar_format) adjustment files, which store photo edit information in XML format. The tool extracts and decodes the `data` block, which is base64-encoded and zlib-compressed, and outputs the decoded data as JSON.

<details>
<summary>Example</summary>

### XML content

```xml
<plist version="1.0">
<dict>
	<key>adjustmentBaseVersion</key>
	<integer>0</integer>
	<key>adjustmentData</key>
	<data>
	vVPJbtswEP0XngWBOyndDCRFc2gC2EAXFDnQ0shioQ0SlQWG/71DKbGdouixcxLmzbz3
	RjM8khaCK11wJD+S1k0Bxs/gD3UguaBcJm+5b74MNcklFTwh/eihCy74viM5PSWk6sfW
	ha8wTkuKJeRp/b7rqj4S72fflPdzu4eR5ITzjRBKkoS4YTh3EUmZTm3KMT8VNbRuC09+
	xWhChsaFqIOF/mFHUNWVv+YptGhlIvnP419cQOf2DZQkD+MMyAoh+O4wRUdugDHMI5Cc
	pyZbQnHBNLcSJzw0bppg+uJCgE3T9M8XkhKGUL/PVbghkpSbf7K17sW3c3spYjohu5uH
	T1voShjR0tk0As3cuvveT7ArXIPFNKWMSsaUsMwKbTPGDP5yV8A6dlH77nssE0ppzYXU
	lhmlBMXlNVCF21f4EWFLKWWMarRmdEaNPcNLN8+k5TzLhEYeJEEnY7yDd1xoZaw0xuBM
	BidDvOunldooY2hmqORaMW4MKkdXC6Y5Z9jEhZUorDJz4V17rZZWWUm55ToTEY+8q6bg
	UrPoSiqbKaZPj/HYinnaQhHiAl4XCS3pdYiEPMc8Ex/zeBEvy6jafsjjiuql3ursOgwe
	Weu7P3aXijdUM2WZ5Oz0fz2hnC/x6H3ll9d0Ew/ytqqi+vtTvLsuKPo2xYfWQDrUfejJ
	6fH0Gw==
	</data>
	<key>adjustmentEditorBundleID</key>
	<string>com.apple.camera</string>
	<key>adjustmentFormatIdentifier</key>
	<string>com.apple.photo</string>
	<key>adjustmentFormatVersion</key>
	<string>1.11</string>
	<key>adjustmentRenderTypes</key>
	<integer>24576</integer>
	<key>adjustmentTimestamp</key>
	<date>2024-10-19T11:37:10Z</date>
</dict>
</plist>
```

### Decoded `<data>` block

```json
{
  "metadata": {
    "masterHeight": 3024,
    "masterWidth": 4032,
    "orientation": 0
  },
  "formatVersion": 1,
  "versionInfo": {
    "buildNumber": "22A3354",
    "appVersion": "4016.8.2",
    "schemaRevision": 0,
    "platform": "iOS"
  },
  "adjustments": [
    {
      "formatVersion": 1,
      "enabled": true,
      "settings": {
        "aperture": 2.799999952316284,
        "glassesMatteAllowed": true,
        "depthInfo": {
          "capturedAperture": 2.799999952316284,
          "maximumAperture": 16,
          "SDOFRenderingVersion": 6,
          "lumaNoiseScale": 0.010411538183689117,
          "faces": [
            {
              "chinX": 0.35566234681755304,
              "leftEyeY": 0.8000110699576908,
              "leftEyeX": 0.29482299363553466,
              "rightEyeX": 0.36578477728471626,
              "noseY": 0.7577097042651277,
              "chinY": 0.622177223849576,
              "rightEyeY": 0.786485840282694,
              "noseX": 0.33246122994589516
            }
          ],
          "focusRect": {
            "y": 0.664,
            "w": 0.134,
            "x": 0.268,
            "h": 0.18699999999999997
          },
          "minimumAperture": 1.399999976158142
        },
        "focusRect": {
          "y": 0.664,
          "w": 0.134,
          "x": 0.268,
          "h": 0.18699999999999997
        }
      },
      "identifier": "DepthEffect",
      "formatIdentifier": "com.apple.photo"
    }
  ]
}
```

</details>

## Features
- Reads AAE XML file
- Decodes and decompresses the `data` block
- Prints decoded data as JSON
- Optionally prints the XML content with the decoded data

## Usage

```
python3 aae-decode.py <AAE_FILE> [--xml]
```

- `<AAE_FILE>`: Path to the AAE file
- `--xml`: (Optional) Print both the XML content and the decoded `data` block. Without this flag, only the decoded data is printed.

### Examples

Print only decoded data:
```
python3 aae-decode.py example.AAE
```

Print XML and decoded data:
```
python3 aae-decode.py example.AAE --xml
```

## Requirements
- Python 3.x

No external dependencies are required; only the Python standard library is used.

## License
MIT License
