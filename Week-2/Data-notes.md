# Data notes

## GRID3 Nigeria Operational Wards v3.0
	- Source: https://data.grid3.org
	- downloaded: 08/09/2026
	- Features: 5872, Polygons
	- Columns: OBJECTID, country, iso3, state, statecode, lga, lga_alt_names, ward, ward_alt_names, ward_v1_grid3, ward_in_grid3_ward_list, multipart_count, source, date, area_sqkm
	- No nulls in ward name
	- Completeness:  My LGA is fully covered
	- Currency: Most recent edits were in July, 2026 
	- Positional: The boundaries fit well with other neighbouring LGA and State boundaries
	- Attribute: It contains the ward names of all wards
	- Fitness: It is quite fit for the site suitability analysis 


### Roads
	- Source: https://data.humdata.org
	- Downloaded: 08/09/2026
	- 1756750 features, lines
	- Columns: fid, id, name, name_en, name_yo, highway, smoothness, width, lanes, surface, layer, bridge, source, oneway, adm0_pcode, adm0_name, adm1_pcode, adm1_name, adm2_pcode, adm2_name, adm3_pcode, adm3_name, adm4_pcode, adm4_name, name_latin
	- Many have no surface tag, no lanes tag, no name tag
	- The LGA is fully covered
	- Completeness: The coverage is complete in the built-up area, however a few streets are missing within the rural areas
	- Currency: Most recent edits were on the 6th September, 2026 
	- Positional: The roads align well with satellite imagery
	- Attribute: Only 3.6% carry a surface attribute tag. However, they all have their highway attribute tag.
	- Fitness: It is quite fit for the site suitability analysis 

	
#### GRID3 NGA Health Facility
	- Source: https://data.grid3.org
	- Downloaded: 08/09/2026
	- Features: 350, point
	- Columns: OBJECTID, unique_id, latitude, longitude, country, iso, state_standard, lga_standard, ward_standard, ward_bdry, ward_in_grid3_ward_list, facility_name, alt_name, settlement_name,- facility_level, facility_type, facility_ownership, facility_ownership_type, functional, date_created, sett_ext_type, mgrs_code, input_data_record_ids, input_data_sources, nhfr_facility_code, gps_accuracy, sett_ext_dist_m, dist_ward_grid3_bdry_km, flag1, flag2, flag3, flag4, flag5, flag6, issues, flag_count
	- LGA is fully covered
	- Completeness: The coverage looks complete in the built-up area, however a the presence of facilities are sparse within the rural areas. Nonetheless, this is as expected
	- Currency: Most recent edits were August, 2026 
	- Positional: The points align with known primary health facilities on a satellite imagery
	- Attribute: Carries appropriate health facility type tag
	- Fitness: It is quite fit for the site suitability analysis 


##### Rivers
	- Source: https://data.humdata.org
	- Downloaded: 08/09/2026
	- Features: 1527551, lines
	- Columns: OBJECTID, HYRIV_ID, NEXT_DOWN, MAIN_RIV, LENGTH_KM, DIST_DN_KM, DIST_UP_KM, CATCH_SKM, UPLAND_SKM, ENDORHEIC, DIS_AV_CMS, ORD_STRA, ORD_CLAS, ORD_FLOW, HYBAS_L12, Shape_Length
	- LGA is fully covered
	- Completeness: The coverage is complete in the the LGA
	- Currency: Most recent edits were in March, 2025
	- Positional: It aligns well with known rivers, however there are also plotted lines that have no correlating physical existence. This can be corrected by editing under a high imagery satellite map
	- Attribute: They all contain all necessary tag
	- Fitness: It is quite fit for the site suitability analysis 

###### CRS and Preparation
	- All source data arrived in EPSG:4326 (WGS84)
	- Study Area: Sapele LGA, extracted from GRID3 Wards
	- All layer were reprojected to ESPG:32631 (UTM 31N), then clipped to the study area
	- Area Check: Sapele 424km2
	- Working files in data/processed/, raw files untouched in data/raw
