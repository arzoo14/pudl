"""Resource metadata."""
from typing import Any, Dict, List

from .helpers import build_foreign_keys

RESOURCE_METADATA: Dict[str, Dict[str, Any]] = {
    "accumulated_depreciation_ferc1": {
        "description": "Balances and changes to FERC Accumulated Provision for Depreciation.",
        "schema": {
            "fields": [
                "utility_id_ferc1",
                "report_year",
                "record_id",
                "line_id",
                "total",
                "electric_plant",
                "future_plant",
                "leased_plant",
            ],
            "primary_key": ["utility_id_ferc1", "report_year", "line_id"],
        },
        "sources": ["ferc1"],
    },
    "assn_gen_eia_unit_epa": {
        "schema": {
            "fields": [
                "generator_id",
                "plant_id_eia",
                "unit_id_epa",
            ],
        }
    },
    "assn_plant_id_eia_epa": {
        "schema": {
            "fields": [
                "plant_id_eia",
                "plant_id_epa",
            ],
        }
    },
    "boiler_fuel_eia923": {
        "schema": {
            "fields": [
                "plant_id_eia",
                "boiler_id",
                "fuel_type_code",
                "fuel_type_code_pudl",
                "report_date",
                "fuel_consumed_units",
                "fuel_mmbtu_per_unit",
                "sulfur_content_pct",
                "ash_content_pct",
            ],
            # Need to fix transform function to ensure this natural primary key
            # See https://github.com/catalyst-cooperative/pudl/issues/852
            # "primary_key": [
            #     "plant_id_eia",
            #     "boiler_id",
            #     "fuel_type_code",
            #     "report_date"
            # ],
        },
        "sources": ["eia923"],
    },
    "boiler_generator_assn_eia860": {
        "schema": {
            "fields": [
                "plant_id_eia",
                "report_date",
                "generator_id",
                "boiler_id",
                "unit_id_eia",
                "unit_id_pudl",
                "bga_source",
            ],
            "primary_key": ["plant_id_eia", "report_date", "generator_id", "boiler_id"],
        },
        "sources": ["eia860"],
    },
    "boilers_entity_eia": {
        "schema": {
            "fields": ["plant_id_eia", "boiler_id", "prime_mover_code"],
            "primary_key": ["plant_id_eia", "boiler_id"],
            "foreign_key_rules": {"fields": [["plant_id_eia", "boiler_id"]]},
        },
    },
    "coalmine_eia923": {
        "schema": {
            "fields": [
                "mine_id_pudl",
                "mine_name",
                "mine_type_code",
                "state",
                "county_id_fips",
                "mine_id_msha",
            ],
            "primary_key": ["mine_id_pudl"],
            "foreign_key_rules": {"fields": [["mine_id_pudl"]]},
        },
        "sources": ["eia923"],
    },
    "datasets": {
        "schema": {"fields": ["datasource", "active"], "primary_key": ["datasource"]},
    },
    "energy_sources_eia": {
        "schema": {
            "fields": ["abbr", "energy_source"],
            "primary_key": ["abbr"],
            "foreign_key_rules": {
                "fields": [
                    ["energy_source_code"],
                    ["fuel_type"],
                    ["fuel_type_code"],
                ],
                "exclude": ["plants_small_ferc1", "fuel_types_aer_eia"]
            },
        },
        "sources": ["eia923"],
    },
    "ferc_accounts": {
        "description": "Account numbers from the FERC Uniform System of Accounts for Electric Plant, which is defined in Code of Federal Regulations (CFR) Title 18, Chapter I, Subchapter C, Part 101. (See e.g. https://www.law.cornell.edu/cfr/text/18/part-101).",
        "schema": {
            "fields": ["ferc_account_id", "ferc_account_description"],
            "primary_key": ["ferc_account_id"],
        },
    },
    "ferc_depreciation_lines": {
        "description": "PUDL assigned FERC Form 1 line identifiers and long descriptions from FERC Form 1 page 219, Accumulated Provision for Depreciation of Electric Utility Plant (Account 108).",
        "schema": {
            "fields": ["line_id", "ferc_account_description"],
            "primary_key": ["line_id"],
            "foreign_key_rules": {"fields": [["line_id"]]},
        },
    },
    "fuel_ferc1": {
        "description": "Annual fuel cost and quanitiy for steam plants with a capacity of 25+ MW, internal combustion and gas-turbine plants of 10+ MW, and all nuclear plants. As reported on page 402 of FERC Form 1 and extracted from the f1_fuel table in FERC's FoxPro Database.",
        "schema": {
            "fields": [
                "record_id",
                "utility_id_ferc1",
                "report_year",
                "plant_name_ferc1",
                "fuel_type_code_pudl",
                "fuel_unit",
                "fuel_qty_burned",
                "fuel_mmbtu_per_unit",
                "fuel_cost_per_unit_burned",
                "fuel_cost_per_unit_delivered",
                "fuel_cost_per_mmbtu",
            ],
        },
    },
    "fuel_receipts_costs_eia923": {
        "schema": {
            "fields": [
                "plant_id_eia",
                "report_date",
                "contract_type_code",
                "contract_expiration_date",
                "energy_source_code",
                "fuel_type_code_pudl",
                "fuel_group_code",
                "fuel_group_code_simple",
                "mine_id_pudl",
                "supplier_name",
                "fuel_qty_units",
                "heat_content_mmbtu_per_unit",
                "sulfur_content_pct",
                "ash_content_pct",
                "mercury_content_ppm",
                "fuel_cost_per_mmbtu",
                "primary_transportation_mode_code",
                "secondary_transportation_mode_code",
                "natural_gas_transport_code",
                "natural_gas_delivery_contract_type_code",
                "moisture_content_pct",
                "chlorine_content_ppm",
            ],
        },
        "sources": ["eia923"],
    },
    "fuel_types_aer_eia": {
        "schema": {
            "fields": ["abbr", "fuel_type"],
            "primary_key": ["abbr"],
            "foreign_key_rules": {"fields": [["fuel_type_code_aer"]]},
        },
        "sources": ["eia923"],
    },
    "generation_eia923": {
        "schema": {
            "fields": [
                "plant_id_eia",
                "generator_id",
                "report_date",
                "net_generation_mwh",
            ],
            # Null values in the generator_id field. See:
            # https://github.com/catalyst-cooperative/pudl/issues/1208
            # "primary_key": ["plant_id_eia", "generator_id", "report_date"],
        },
        "sources": ["eia923"],
    },
    "generation_fuel_eia923": {
        "schema": {
            "fields": [
                "plant_id_eia",
                "report_date",
                "nuclear_unit_id",
                "fuel_type",
                "fuel_type_code_pudl",
                "fuel_type_code_aer",
                "prime_mover_code",
                "fuel_consumed_units",
                "fuel_consumed_for_electricity_units",
                "fuel_mmbtu_per_unit",
                "fuel_consumed_mmbtu",
                "fuel_consumed_for_electricity_mmbtu",
                "net_generation_mwh",
            ],
            # Need to fix transform function to ensure this natural primary key
            # See https://github.com/catalyst-cooperative/pudl/issues/851
            # "primary_key": [
            #     "plant_id_eia",
            #     "report_date",
            #     "nuclear_unit_id",
            #     "fuel_type",
            #     "prime_mover_code"
            # ],
        },
        "sources": ["eia923"],
    },
    "generators_eia860": {
        "schema": {
            "fields": [
                "plant_id_eia",
                "generator_id",
                "report_date",
                "operational_status_code",
                "operational_status",
                "ownership_code",
                "utility_id_eia",
                "capacity_mw",
                "summer_capacity_mw",
                "summer_capacity_estimate",
                "winter_capacity_mw",
                "winter_capacity_estimate",
                "energy_source_code_1",
                "energy_source_code_2",
                "energy_source_code_3",
                "energy_source_code_4",
                "energy_source_code_5",
                "energy_source_code_6",
                "energy_source_1_transport_1",
                "energy_source_1_transport_2",
                "energy_source_1_transport_3",
                "energy_source_2_transport_1",
                "energy_source_2_transport_2",
                "energy_source_2_transport_3",
                "fuel_type_code_pudl",
                "multiple_fuels",
                "deliver_power_transgrid",
                "distributed_generation",
                "syncronized_transmission_grid",
                "turbines_num",
                "planned_modifications",
                "planned_net_summer_capacity_uprate_mw",
                "planned_net_winter_capacity_uprate_mw",
                "planned_uprate_date",
                "planned_net_summer_capacity_derate_mw",
                "planned_net_winter_capacity_derate_mw",
                "planned_derate_date",
                "planned_new_prime_mover_code",
                "planned_energy_source_code_1",
                "planned_repower_date",
                "other_planned_modifications",
                "other_modifications_date",
                "planned_retirement_date",
                "carbon_capture",
                "startup_source_code_1",
                "startup_source_code_2",
                "startup_source_code_3",
                "startup_source_code_4",
                "technology_description",
                "turbines_inverters_hydrokinetics",
                "time_cold_shutdown_full_load_code",
                "planned_new_capacity_mw",
                "cofire_fuels",
                "switch_oil_gas",
                "nameplate_power_factor",
                "minimum_load_mw",
                "uprate_derate_during_year",
                "uprate_derate_completed_date",
                "current_planned_operating_date",
                "summer_estimated_capability_mw",
                "winter_estimated_capability_mw",
                "retirement_date",
                "owned_by_non_utility",
                "reactive_power_output_mvar",
                "data_source",
            ],
            "primary_key": ["plant_id_eia", "generator_id", "report_date"],
            "foreign_key_rules": {
                "fields": [["plant_id_eia", "generator_id", "report_date"]],
                # TODO: Excluding monthly data tables since their report_date
                # values don't match up with generators_eia860, which is annual,
                # so non-january records violate the constraint.
                # See: https://github.com/catalyst-cooperative/pudl/issues/1196
                "exclude": [
                    "boiler_fuel_eia923",
                    "fuel_receipts_costs_eia923",
                    "generation_eia923",
                    "generation_fuel_eia923",
                ]
            },
        },
        "sources": ["eia860"],
    },
    "generators_entity_eia": {
        "schema": {
            "fields": [
                "plant_id_eia",
                "generator_id",
                "prime_mover_code",
                "duct_burners",
                "operating_date",
                "topping_bottoming_code",
                "solid_fuel_gasification",
                "pulverized_coal_tech",
                "fluidized_bed_tech",
                "subcritical_tech",
                "supercritical_tech",
                "ultrasupercritical_tech",
                "stoker_tech",
                "other_combustion_tech",
                "bypass_heat_recovery",
                "rto_iso_lmp_node_id",
                "rto_iso_location_wholesale_reporting_id",
                "associated_combined_heat_power",
                "original_planned_operating_date",
                "operating_switch",
                "previously_canceled",
            ],
            "primary_key": ["plant_id_eia", "generator_id"],
            "foreign_key_rules": {"fields": [["plant_id_eia", "generator_id"]]},
        },
    },
    "hourly_emissions_epacems": {
        "schema": {
            "fields": [
                "state",
                "plant_id_eia",
                "unitid",
                "operating_datetime_utc",
                "operating_time_hours",
                "gross_load_mw",
                "steam_load_1000_lbs",
                "so2_mass_lbs",
                "so2_mass_measurement_code",
                "nox_rate_lbs_mmbtu",
                "nox_rate_measurement_code",
                "nox_mass_lbs",
                "nox_mass_measurement_code",
                "co2_mass_tons",
                "co2_mass_measurement_code",
                "heat_content_mmbtu",
                "facility_id",
                "unit_id_epa",
            ],
            "primary_key": ["plant_id_eia", "unitid", "operating_datetime_utc"],
        },
        "group": "epacems",
        "sources": ["epacems"],
    },
    "natural_gas_transport_eia923": {
        "schema": {"fields": ["abbr", "status"], "primary_key": ["abbr"]},
        "sources": ["eia923"],
    },
    "ownership_eia860": {
        "schema": {
            "fields": [
                "report_date",
                "utility_id_eia",
                "plant_id_eia",
                "generator_id",
                "owner_utility_id_eia",
                "owner_name",
                "owner_state",
                "owner_city",
                "owner_street_address",
                "owner_zip_code",
                "fraction_owned",
            ],
            # Currently there are NULL falues in some of these fields. This needs
            # to be fixed in the transform process. See this Github issue:
            # https://github.com/catalyst-cooperative/pudl/issues/1207
            # "primary_key": [
            #     "report_date", "plant_id_eia", "generator_id", "owner_utility_id_eia"
            # ],
        },
        "sources": ["eia860"],
    },
    "plant_in_service_ferc1": {
        "description": "Balances and changes to FERC Electric Plant in Service accounts, as reported on FERC Form 1. Data originally from the f1_plant_in_srvce table in FERC's FoxPro database. Account numbers correspond to the FERC Uniform System of Accounts for Electric Plant, which is defined in Code of Federal Regulations (CFR) Title 18, Chapter I, Subchapter C, Part 101. (See e.g. https://www.law.cornell.edu/cfr/text/18/part-101). Each FERC respondent reports starting and ending balances for each account annually. Balances are organization wide, and are not broken down on a per-plant basis. End of year balance should equal beginning year balance plus the sum of additions, retirements, adjustments, and transfers.",
        "schema": {
            "fields": [
                "utility_id_ferc1",
                "report_year",
                "amount_type",
                "record_id",
                "distribution_acct360_land",
                "distribution_acct361_structures",
                "distribution_acct362_station_equip",
                "distribution_acct363_storage_battery_equip",
                "distribution_acct364_poles_towers",
                "distribution_acct365_overhead_conductors",
                "distribution_acct366_underground_conduit",
                "distribution_acct367_underground_conductors",
                "distribution_acct368_line_transformers",
                "distribution_acct369_services",
                "distribution_acct370_meters",
                "distribution_acct371_customer_installations",
                "distribution_acct372_leased_property",
                "distribution_acct373_street_lighting",
                "distribution_acct374_asset_retirement",
                "distribution_total",
                "electric_plant_in_service_total",
                "electric_plant_purchased_acct102",
                "electric_plant_sold_acct102",
                "experimental_plant_acct103",
                "general_acct389_land",
                "general_acct390_structures",
                "general_acct391_office_equip",
                "general_acct392_transportation_equip",
                "general_acct393_stores_equip",
                "general_acct394_shop_equip",
                "general_acct395_lab_equip",
                "general_acct396_power_operated_equip",
                "general_acct397_communication_equip",
                "general_acct398_misc_equip",
                "general_acct399_1_asset_retirement",
                "general_acct399_other_property",
                "general_subtotal",
                "general_total",
                "hydro_acct330_land",
                "hydro_acct331_structures",
                "hydro_acct332_reservoirs_dams_waterways",
                "hydro_acct333_wheels_turbines_generators",
                "hydro_acct334_accessory_equip",
                "hydro_acct335_misc_equip",
                "hydro_acct336_roads_railroads_bridges",
                "hydro_acct337_asset_retirement",
                "hydro_total",
                "intangible_acct301_organization",
                "intangible_acct302_franchises_consents",
                "intangible_acct303_misc",
                "intangible_total",
                "major_electric_plant_acct101_acct106_total",
                "nuclear_acct320_land",
                "nuclear_acct321_structures",
                "nuclear_acct322_reactor_equip",
                "nuclear_acct323_turbogenerators",
                "nuclear_acct324_accessory_equip",
                "nuclear_acct325_misc_equip",
                "nuclear_acct326_asset_retirement",
                "nuclear_total",
                "other_acct340_land",
                "other_acct341_structures",
                "other_acct342_fuel_accessories",
                "other_acct343_prime_movers",
                "other_acct344_generators",
                "other_acct345_accessory_equip",
                "other_acct346_misc_equip",
                "other_acct347_asset_retirement",
                "other_total",
                "production_total",
                "rtmo_acct380_land",
                "rtmo_acct381_structures",
                "rtmo_acct382_computer_hardware",
                "rtmo_acct383_computer_software",
                "rtmo_acct384_communication_equip",
                "rtmo_acct385_misc_equip",
                "rtmo_total",
                "steam_acct310_land",
                "steam_acct311_structures",
                "steam_acct312_boiler_equip",
                "steam_acct313_engines",
                "steam_acct314_turbogenerators",
                "steam_acct315_accessory_equip",
                "steam_acct316_misc_equip",
                "steam_acct317_asset_retirement",
                "steam_total",
                "transmission_acct350_land",
                "transmission_acct352_structures",
                "transmission_acct353_station_equip",
                "transmission_acct354_towers",
                "transmission_acct355_poles",
                "transmission_acct356_overhead_conductors",
                "transmission_acct357_underground_conduit",
                "transmission_acct358_underground_conductors",
                "transmission_acct359_1_asset_retirement",
                "transmission_acct359_roads_trails",
                "transmission_total",
            ],
            "primary_key": ["utility_id_ferc1", "report_year", "amount_type"],
        },
        "sources": ["ferc1"],
    },
    "plant_unit_epa": {
        "schema": {
            "fields": ["plant_id_epa", "unit_id_epa"],
        }
    },
    "plants_eia": {
        "schema": {
            "fields": ["plant_id_eia", "plant_name_eia", "plant_id_pudl"],
            "primary_key": ["plant_id_eia"],
        },
    },
    "plants_eia860": {
        "schema": {
            "fields": [
                "plant_id_eia",
                "report_date",
                "ash_impoundment",
                "ash_impoundment_lined",
                "ash_impoundment_status",
                "datum",
                "energy_storage",
                "ferc_cogen_docket_no",
                "ferc_exempt_wholesale_generator_docket_no",
                "ferc_small_power_producer_docket_no",
                "liquefied_natural_gas_storage",
                "natural_gas_local_distribution_company",
                "natural_gas_storage",
                "natural_gas_pipeline_name_1",
                "natural_gas_pipeline_name_2",
                "natural_gas_pipeline_name_3",
                "nerc_region",
                "net_metering",
                "pipeline_notes",
                "regulatory_status_code",
                "service_area",
                "transmission_distribution_owner_id",
                "transmission_distribution_owner_name",
                "transmission_distribution_owner_state",
                "utility_id_eia",
                "water_source",
            ],
            "primary_key": ["plant_id_eia", "report_date"],
            "foreign_key_rules": {
                "fields": [["plant_id_eia", "report_date"]],
                # TODO: Excluding monthly data tables since their report_date
                # values don't match up with plants_eia860, which is annual, so
                # non-january records fail.
                # See: https://github.com/catalyst-cooperative/pudl/issues/1196
                "exclude": [
                    "boiler_fuel_eia923",
                    "fuel_receipts_costs_eia923",
                    "generation_eia923",
                    "generation_fuel_eia923",
                ]
            },
        },
        "sources": ["eia860"],
    },
    "plants_entity_eia": {
        "schema": {
            "fields": [
                "plant_id_eia",
                "plant_name_eia",
                "balancing_authority_code_eia",
                "balancing_authority_name_eia",
                "city",
                "county",
                "ferc_cogen_status",
                "ferc_exempt_wholesale_generator",
                "ferc_small_power_producer",
                "grid_voltage_kv",
                "grid_voltage_2_kv",
                "grid_voltage_3_kv",
                "iso_rto_code",
                "latitude",
                "longitude",
                "primary_purpose_naics_id",
                "sector_name",
                "sector_id",
                "state",
                "street_address",
                "zip_code",
                "timezone",
            ],
            "primary_key": ["plant_id_eia"],
            "foreign_key_rules": {
                "fields": [["plant_id_eia"]],
                # Excluding plants_eia because it's static and manually compiled
                # so it has plants from *all* years of data, even when only a
                # restricted set of data is processed, leading to constraint
                # violations.
                # See: https://github.com/catalyst-cooperative/pudl/issues/1196
                "exclude": ["plants_eia"],
            },
        },
    },
    "plants_ferc1": {
        "title": "FERC 1 Plants",
        "schema": {
            "fields": ["utility_id_ferc1", "plant_name_ferc1", "plant_id_pudl"],
            "primary_key": ["utility_id_ferc1", "plant_name_ferc1"],
            "foreign_key_rules": {"fields": [
                ["utility_id_ferc1", "plant_name_ferc1"],
                ["utility_id_ferc1", "plant_name_original"]
            ]},
        },
    },
    "plants_hydro_ferc1": {
        "description": "Hydroelectric generating plant statistics for large plants. Large plants have an installed nameplate capacity of more than 10 MW. As reported on FERC Form 1, pages 406-407, and extracted from the f1_hydro table in FERC's FoxPro database.",
        "schema": {
            "fields": [
                "record_id",
                "utility_id_ferc1",
                "report_year",
                "plant_name_ferc1",
                "project_num",
                "plant_type",
                "construction_type",
                "construction_year",
                "installation_year",
                "capacity_mw",
                "peak_demand_mw",
                "plant_hours_connected_while_generating",
                "net_capacity_favorable_conditions_mw",
                "net_capacity_adverse_conditions_mw",
                "avg_num_employees",
                "net_generation_mwh",
                "capex_land",
                "capex_structures",
                "capex_facilities",
                "capex_equipment",
                "capex_roads",
                "asset_retirement_cost",
                "capex_total",
                "capex_per_mw",
                "opex_operations",
                "opex_water_for_power",
                "opex_hydraulic",
                "opex_electric",
                "opex_generation_misc",
                "opex_rents",
                "opex_engineering",
                "opex_structures",
                "opex_dams",
                "opex_plant",
                "opex_misc_plant",
                "opex_total",
                "opex_per_mwh",
            ],
        },
        "sources": ["ferc1"],
    },
    "plants_pudl": {
        "title": "PUDL Plants",
        "description": "Home table for PUDL assigned plant IDs. These IDs are manually generated each year when new FERC and EIA reporting is integrated, and any newly identified plants are added to the list with a new ID. Each ID maps to a power plant which is reported in at least one FERC or EIA data set. This table is read in from a spreadsheet stored in the PUDL repository: src/pudl/package_data/glue/mapping_eia923_ferc1.xlsx",
        "schema": {
            "fields": ["plant_id_pudl", "plant_name_pudl"],
            "primary_key": ["plant_id_pudl"],
            "foreign_key_rules": {"fields": [["plant_id_pudl"]]},
        },
    },
    "plants_pumped_storage_ferc1": {
        "description": "Generating plant statistics for hydroelectric pumped storage plants with an installed nameplate capacity of 10+ MW. As reported on page 408 of FERC Form 1 and extracted from the f1_pumped_storage table in FERC's FoxPro Database.",
        "schema": {
            "fields": [
                "record_id",
                "utility_id_ferc1",
                "report_year",
                "plant_name_ferc1",
                "project_num",
                "construction_type",
                "construction_year",
                "installation_year",
                "capacity_mw",
                "peak_demand_mw",
                "plant_hours_connected_while_generating",
                "plant_capability_mw",
                "avg_num_employees",
                "net_generation_mwh",
                "energy_used_for_pumping_mwh",
                "net_load_mwh",
                "capex_land",
                "capex_structures",
                "capex_facilities",
                "capex_wheels_turbines_generators",
                "capex_equipment_electric",
                "capex_equipment_misc",
                "capex_roads",
                "asset_retirement_cost",
                "capex_total",
                "capex_per_mw",
                "opex_operations",
                "opex_water_for_power",
                "opex_pumped_storage",
                "opex_electric",
                "opex_generation_misc",
                "opex_rents",
                "opex_engineering",
                "opex_structures",
                "opex_dams",
                "opex_plant",
                "opex_misc_plant",
                "opex_production_before_pumping",
                "opex_pumping",
                "opex_total",
                "opex_per_mwh",
            ],
        },
        "sources": ["ferc1"],
    },
    "plants_small_ferc1": {
        "description": "Generating plant statistics for steam plants with less than 25 MW installed nameplate capacity and internal combustion plants, gas turbine-plants, conventional hydro plants, and pumped storage plants with less than 10 MW installed nameplate capacity. As reported on FERC Form 1 pages 410-411, and extracted from the FERC FoxPro database table f1_gnrt_plant.",
        "schema": {
            "fields": [
                "record_id",
                "utility_id_ferc1",
                "report_year",
                "plant_name_original",
                "plant_name_ferc1",
                "plant_type",
                "ferc_license_id",
                "construction_year",
                "capacity_mw",
                "peak_demand_mw",
                "net_generation_mwh",
                "total_cost_of_plant",
                "capex_per_mw",
                "opex_total",
                "opex_fuel",
                "opex_maintenance",
                "fuel_type",
                "fuel_cost_per_mmbtu",
            ],
        },
        "sources": ["ferc1"],
    },
    "plants_steam_ferc1": {
        "description": "Generating plant statistics for steam plants with a capacity of 25+ MW, internal combustion and gas-turbine plants of 10+ MW, and all nuclear plants. As reported on page 402 of FERC Form 1 and extracted from the f1_gnrt_plant table in FERC's FoxPro Database.",
        "schema": {
            "fields": [
                "record_id",
                "utility_id_ferc1",
                "report_year",
                "plant_id_ferc1",
                "plant_name_ferc1",
                "plant_type",
                "construction_type",
                "construction_year",
                "installation_year",
                "capacity_mw",
                "peak_demand_mw",
                "plant_hours_connected_while_generating",
                "plant_capability_mw",
                "water_limited_capacity_mw",
                "not_water_limited_capacity_mw",
                "avg_num_employees",
                "net_generation_mwh",
                "capex_land",
                "capex_structures",
                "capex_equipment",
                "capex_total",
                "capex_per_mw",
                "opex_operations",
                "opex_fuel",
                "opex_coolants",
                "opex_steam",
                "opex_steam_other",
                "opex_transfer",
                "opex_electric",
                "opex_misc_power",
                "opex_rents",
                "opex_allowances",
                "opex_engineering",
                "opex_structures",
                "opex_boiler",
                "opex_plants",
                "opex_misc_steam",
                "opex_production_total",
                "opex_per_mwh",
                "asset_retirement_cost",
            ],
        },
        "sources": ["ferc1"],
    },
    "prime_movers_eia": {
        "schema": {
            "fields": ["abbr", "prime_mover"],
            "primary_key": ["abbr"],
            "foreign_key_rules": {"fields": [["prime_mover_code"]]},
        },
        "sources": ["eia923", "eia860"],
    },
    "purchased_power_ferc1": {
        "description": "Purchased Power (Account 555) including power exchanges (i.e. transactions involving a balancing of debits and credits for energy, capacity, etc.) and any settlements for imbalanced exchanges. Reported on pages 326-327 of FERC Form 1. Extracted from the f1_purchased_pwr table in FERC's FoxPro database.",
        "schema": {
            "fields": [
                "record_id",
                "utility_id_ferc1",
                "report_year",
                "seller_name",
                "purchase_type",
                "tariff",
                "billing_demand_mw",
                "non_coincident_peak_demand_mw",
                "coincident_peak_demand_mw",
                "purchased_mwh",
                "received_mwh",
                "delivered_mwh",
                "demand_charges",
                "energy_charges",
                "other_charges",
                "total_settlement",
            ]
        },
        "sources": ["ferc1"],
    },
    "fuel_transportation_modes_eia": {
        "schema": {
            "fields": ["abbr", "fuel_transportation_mode"],
            "primary_key": ["abbr"],
            "foreign_key_rules": {"fields": [
                ["primary_transportation_mode_code"],
                ["secondary_transportation_mode_code"],
            ]},
        },
        "sources": ["eia923"],
    },
    "utilities_eia": {
        "schema": {
            "fields": ["utility_id_eia", "utility_name_eia", "utility_id_pudl"],
            "primary_key": ["utility_id_eia"],
        },
    },
    "utilities_eia860": {
        "schema": {
            "fields": [
                "utility_id_eia",
                "report_date",
                "street_address",
                "city",
                "state",
                "zip_code",
                "plants_reported_owner",
                "plants_reported_operator",
                "plants_reported_asset_manager",
                "plants_reported_other_relationship",
                "entity_type",
                "attention_line",
                "address_2",
                "zip_code_4",
                "contact_firstname",
                "contact_lastname",
                "contact_title",
                "phone_number",
                "phone_extension",
                "contact_firstname_2",
                "contact_lastname_2",
                "contact_title_2",
                "phone_number_2",
                "phone_extension_2",

            ],
            "primary_key": ["utility_id_eia", "report_date"],
            "foreign_key_rules": {"fields": [
                ["utility_id_eia", "report_date"],
                # Failing because this column is not harvested in the old
                # system. TODO: re-enable when we switch to new system. See:
                # https://github.com/catalyst-cooperative/pudl/issues/1196
                # ["owner_utility_id_eia", "report_date"],
            ]},
        },
        "sources": ["eia860"],
    },
    "utilities_entity_eia": {
        "schema": {
            "fields": ["utility_id_eia", "utility_name_eia"],
            "primary_key": ["utility_id_eia"],
            "foreign_key_rules": {
                "fields": [
                    ["utility_id_eia"],
                    # Results in constraint failures because this column is not
                    # harvested in the old system. See:
                    # https://github.com/catalyst-cooperative/pudl/issues/1196
                    # ["owner_utility_id_eia"]
                ],
                # Excluding utilities_eia b/c it's static and manually compiled
                # so it has utilities from *all* years of data, even when only a
                # restricted set of data is processed, leading to constraint
                # violations.
                # See: https://github.com/catalyst-cooperative/pudl/issues/1196
                "exclude": ["utilities_eia"],
            },
        },
    },
    "utilities_ferc1": {
        "description": "This table maps the manually assigned PUDL utility ID to a FERC respondent ID, enabling a connection between the FERC and EIA data sets. It also stores the utility name associated with the FERC respondent ID. Those values originate in the f1_respondent_id table in FERC's FoxPro database, which is stored in a file called F1_1.DBF. This table is generated from a spreadsheet stored in the PUDL repository: results/id_mapping/mapping_eia923_ferc1.xlsx",
        "schema": {
            "fields": ["utility_id_ferc1", "utility_name_ferc1", "utility_id_pudl"],
            "primary_key": ["utility_id_ferc1"],
            "foreign_key_rules": {"fields": [["utility_id_ferc1"]]},
        },
    },
    "utilities_pudl": {
        "title": "PUDL Utilities",
        "description": "Home table for PUDL assigned utility IDs. These IDs are manually generated each year when new FERC and EIA reporting is integrated, and any newly found utilities are added to the list with a new ID. Each ID maps to a power plant owning or operating entity which is reported in at least one FERC or EIA data set. This table is read in from a spreadsheet stored in the PUDL repository: src/pudl/package_data/glue/mapping_eia923_ferc1.xlsx",
        "schema": {
            "fields": ["utility_id_pudl", "utility_name_pudl"],
            "primary_key": ["utility_id_pudl"],
            "foreign_key_rules": {"fields": [["utility_id_pudl"]]},
        },
    },
    "utility_plant_assn": {
        "schema": {
            "fields": ["utility_id_pudl", "plant_id_pudl"],
            "primary_key": ["utility_id_pudl", "plant_id_pudl"],
        },
    },
}
"""
Resource attributes by PUDL identifier (`resource.name`).

Keys are in alphabetical order.
Each element of `sources` and `licenses` may be a dictionary or a PUDL identifier.

See :func:`.helpers.build_foreign_keys` for the expected format of `foreign_key_rules`.
"""

FOREIGN_KEYS: Dict[str, List[dict]] = build_foreign_keys(RESOURCE_METADATA)
"""
Foreign keys by resource name.

See :func:`.helpers.build_foreign_keys`.
"""
