import sys
import xml.etree.ElementTree as ET
import base64
import zlib
import json

def main():

	show_xml = False
	args = sys.argv[1:]
	if '--xml' in args:
		show_xml = True
		args.remove('--xml')
	if not args:
		print("AAE Decode Utility")
		print("Usage: python3 aae-decode.py <AAE_FILE> [--xml]")
		print("Outputs decoded <data> block from an AAE XML file, or the entire XML if --xml is specified.")		
		sys.exit(1)
	aae_file = args[0]

	try:
		tree = ET.parse(aae_file)
		root = tree.getroot()
		data_elem = root.find('.//data')
		if data_elem is None or not data_elem.text:
			print("No <data> block found in XML.")
			sys.exit(2)
		data_str = ''.join(data_elem.text.split())
		decoded = base64.b64decode(data_str)
		unzipped = zlib.decompress(decoded, -zlib.MAX_WBITS)
		try:
			decoded_json = json.loads(unzipped)
			output_json = json.dumps(decoded_json, indent=2)
		except Exception:
			output_json = unzipped.decode(errors='replace')

		if show_xml:
			print("--- XML content ---")
			ET.dump(root)
			print("\n--- Decoded <data> block ---")
			print(output_json)
		else:
			print(output_json)
	except Exception as e:
		print(f"Error: {e}")
		sys.exit(2)

if __name__ == "__main__":
	main()
