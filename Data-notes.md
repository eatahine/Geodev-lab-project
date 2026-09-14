# Data notes

## GRID3 Nigeria Operational Wards v3.0
	- Source: https://data.grid3.org
	- downloaded: 08/09/2026
	- Features: 5872, Polygons
	- Columns: OBJECTID, country, iso3, state, statecode, lga, lga_alt_names, ward, ward_alt_names, ward_v1_grid3, ward_in_grid3_ward_list, multipart_count, source, date, area_sqkm
	- No nulls in ward name
	- My LGA is fully covered

## Roads
	- Source: https://data.humdata.org
	- Downloaded: 08/09/2026
	- 1756750 features, lines
	- Columns: fid, id, name, name_en, name_yo, highway, smoothness, width, lanes, surface, layer, bridge, source, oneway, adm0_pcode, adm0_name, adm1_pcode, adm1_name, adm2_pcode, adm2_name, adm3_pcode, adm3_name, adm4_pcode, adm4_name, name_latin
	- Many have no surface tag, no lanes tag, no name tag
	- The LGA is fully covered

	
#### GRID3 NGA Health Facility
	- Source: https://data.grid3.org
	- Downloaded: 08/09/2026
	- Features: 350, point
	- Columns: OBJECTID, unique_id, latitude, longitude, country, iso, state_standard, lga_standard, ward_standard, ward_bdry, ward_in_grid3_ward_list, facility_name, alt_name, settlement_name,- facility_level, facility_type, facility_ownership, facility_ownership_type, functional, date_created, sett_ext_type, mgrs_code, input_data_record_ids, input_data_sources, nhfr_facility_code, gps_accuracy, sett_ext_dist_m, dist_ward_grid3_bdry_km, flag1, flag2, flag3, flag4, flag5, flag6, issues, flag_count
	- LGA is fully covered

