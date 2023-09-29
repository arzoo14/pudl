"""Definitions of data tables primarily coming from EIA-860."""
from typing import Any

RESOURCE_METADATA: dict[str, dict[str, Any]] = {
    "boilers_eia860": {
        "description": (
            "Annually varying boiler attributes, compiled from across all EIA-860 data."
        ),
        "schema": {
            "fields": [
                "plant_id_eia",
                "boiler_id",
                "report_date",
                "boiler_operating_date",
                "boiler_status",
                "boiler_retirement_date",
                "boiler_type",
                "firing_type_1",
                "firing_type_2",
                "firing_type_3",
                "firing_rate_using_coal_tons_per_hour",
                "firing_rate_using_oil_bbls_per_hour",
                "firing_rate_using_gas_mcf_per_hour",
                "firing_rate_using_other_fuels",
                "boiler_fuel_code_1",
                "boiler_fuel_code_2",
                "boiler_fuel_code_3",
                "boiler_fuel_code_4",
                "waste_heat_input_mmbtu_per_hour",
                "wet_dry_bottom",
                "fly_ash_reinjection",
                "hrsg",
                "max_steam_flow_1000_lbs_per_hour",
                "turndown_ratio",
                "efficiency_100pct_load",
                "efficiency_50pct_load",
                "air_flow_100pct_load_cubic_feet_per_minute",
                "new_source_review",
                "new_source_review_date",
                "new_source_review_permit",
                "regulation_particulate",
                "regulation_so2",
                "regulation_nox",
                "standard_particulate_rate",
                "standard_so2_rate",
                "standard_nox_rate",
                "unit_particulate",
                "unit_so2",
                "unit_nox",
                "compliance_year_particulate",
                "compliance_year_nox",
                "compliance_year_so2",
                "particulate_control_out_of_compliance_strategy_1",
                "particulate_control_out_of_compliance_strategy_2",
                "particulate_control_out_of_compliance_strategy_3",
                "so2_control_out_of_compliance_strategy_1",
                "so2_control_out_of_compliance_strategy_2",
                "so2_control_out_of_compliance_strategy_3",
                "so2_control_existing_caaa_compliance_strategy_1",
                "so2_control_existing_caaa_compliance_strategy_2",
                "so2_control_existing_caaa_compliance_strategy_3",
                "so2_control_planned_caaa_compliance_strategy_1",
                "so2_control_planned_caaa_compliance_strategy_2",
                "so2_control_planned_caaa_compliance_strategy_3",
                "nox_control_out_of_compliance_strategy_1",
                "nox_control_out_of_compliance_strategy_2",
                "nox_control_out_of_compliance_strategy_3",
                "nox_control_existing_caaa_compliance_strategy_1",
                "nox_control_existing_caaa_compliance_strategy_2",
                "nox_control_existing_caaa_compliance_strategy_3",
                "nox_control_planned_caaa_compliance_strategy_1",
                "nox_control_planned_caaa_compliance_strategy_2",
                "nox_control_planned_caaa_compliance_strategy_3",
                "compliance_year_mercury",
                "mercury_control_existing_strategy_1",
                "mercury_control_existing_strategy_2",
                "mercury_control_existing_strategy_3",
                "mercury_control_existing_strategy_4",
                "mercury_control_existing_strategy_5",
                "mercury_control_existing_strategy_6",
                "mercury_control_proposed_strategy_1",
                "mercury_control_proposed_strategy_2",
                "mercury_control_proposed_strategy_3",
                "nox_control_existing_strategy_1",
                "nox_control_existing_strategy_2",
                "nox_control_existing_strategy_3",
                "nox_control_manufacturer",
                "nox_control_manufacturer_code",
                "nox_control_proposed_strategy_1",
                "nox_control_proposed_strategy_2",
                "nox_control_proposed_strategy_3",
                "nox_control_status_code",
                "regulation_mercury",
                "so2_control_existing_strategy_1",
                "so2_control_existing_strategy_2",
                "so2_control_existing_strategy_3",
                "so2_control_proposed_strategy_1",
                "so2_control_proposed_strategy_2",
                "so2_control_proposed_strategy_3",
                "standard_so2_percent_scrubbed",
                "data_maturity",
            ],
            "primary_key": ["plant_id_eia", "boiler_id", "report_date"],
            "foreign_key_rules": {
                "fields": [["plant_id_eia", "boiler_id", "report_date"]],
                # TODO: Excluding monthly data tables since their report_date
                # values don't match up with generators_eia860, which is annual,
                # so non-january records violate the constraint.
                # See: https://github.com/catalyst-cooperative/pudl/issues/1196
                "exclude": [
                    "boiler_fuel_eia923",
                    "denorm_boiler_fuel_eia923",
                    "denorm_boiler_fuel_monthly_eia923",
                ],
            },
        },
        "field_namespace": "eia",
        "sources": ["eia860", "eia923"],
        "etl_group": "eia860",
    },
    "boiler_generator_assn_eia860": {
        "description": (
            "Associations between boilers and generators as reported in EIA-860 "
            "Schedule 6, Part A. Augmented with various heuristics within PUDL."
        ),
        "schema": {
            "fields": [
                "plant_id_eia",
                "report_date",
                "generator_id",
                "boiler_id",
                "unit_id_eia",
                "unit_id_pudl",
                "boiler_generator_assn_type_code",
                "steam_plant_type_code",
                "bga_source",
                "data_maturity",
            ],
            "primary_key": ["plant_id_eia", "report_date", "generator_id", "boiler_id"],
        },
        "field_namespace": "eia",
        "sources": ["eia860", "eia923"],
        "etl_group": "eia860",
    },
    "generators_eia860": {
        "description": (
            "Annually varying generator attributes compiled from across EIA-860 and "
            "EIA-923 data."
        ),
        "schema": {
            "fields": [
                "plant_id_eia",
                "generator_id",
                "utility_id_eia",
                "report_date",
                "operational_status_code",
                "operational_status",
                "ownership_code",
                "capacity_mw",
                "summer_capacity_mw",
                "summer_capacity_estimate",
                "winter_capacity_mw",
                "winter_capacity_estimate",
                "net_capacity_mwdc",
                "energy_storage_capacity_mwh",
                "prime_mover_code",
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
                "planned_generator_retirement_date",
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
                "current_planned_generator_operating_date",
                "summer_estimated_capability_mw",
                "winter_estimated_capability_mw",
                "generator_retirement_date",
                "owned_by_non_utility",
                "reactive_power_output_mvar",
                "ferc_qualifying_facility",
                "data_maturity",
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
                    "capacity_factor_by_generator_monthly",
                    "denorm_generation_eia923",
                    "denorm_generation_monthly_eia923",
                    "fuel_cost_by_generator_monthly",
                    "fuel_receipts_costs_eia923",
                    "generation_eia923",
                    "generation_fuel_by_generator_energy_source_monthly_eia923",
                    "generation_fuel_by_generator_monthly_eia923",
                    "generation_fuel_eia923",
                    "heat_rate_by_generator_monthly",
                    "mcoe_monthly",
                    "mcoe_generators_monthly",
                ],
            },
        },
        "field_namespace": "eia",
        "sources": ["eia860", "eia923"],
        "etl_group": "eia860",
    },
    "ownership_eia860": {
        "description": (
            "Generator Ownership, reported in EIA-860 Schedule 4. Includes only "
            "jointly or third-party owned generators."
        ),
        "schema": {
            "fields": [
                "report_date",
                "owner_utility_id_eia",
                "plant_id_eia",
                "generator_id",
                "owner_utility_name_eia",
                "owner_state",
                "owner_city",
                "owner_country",
                "owner_street_address",
                "owner_zip_code",
                "fraction_owned",
                "data_maturity",
            ],
            "primary_key": [
                "report_date",
                "plant_id_eia",
                "generator_id",
                "owner_utility_id_eia",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia860"],
        "etl_group": "eia860",
    },
    "denorm_ownership_eia860": {
        "description": (
            "Generator Ownership, reported in EIA-860 Schedule 4. Includes only "
            "jointly or third-party owned generators. Denormalized to include plant "
            "and utility names and other associated IDs."
        ),
        "schema": {
            "fields": [
                "report_date",
                "plant_id_eia",
                "plant_id_pudl",
                "plant_name_eia",
                "owner_utility_id_eia",
                # "utility_id_pudl",
                "owner_utility_name_eia",
                "generator_id",
                "state",
                "owner_city",
                "owner_country",
                "owner_street_address",
                "owner_zip_code",
                "fraction_owned",
                "data_maturity",
            ],
            "primary_key": [
                "report_date",
                "plant_id_eia",
                "generator_id",
                "owner_utility_id_eia",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia860"],
        "etl_group": "outputs",
    },
    "plants_eia860": {
        "description": (
            "Annually varying plant attributes, compiled from across all EIA-860 and "
            "EIA-923 data."
        ),
        "schema": {
            "fields": [
                "plant_id_eia",
                "report_date",
                "ash_impoundment",
                "ash_impoundment_lined",
                "ash_impoundment_status",
                "balancing_authority_code_eia",
                "balancing_authority_name_eia",
                "datum",
                "energy_storage",
                "ferc_cogen_docket_no",
                "ferc_cogen_status",
                "ferc_exempt_wholesale_generator_docket_no",
                "ferc_exempt_wholesale_generator",
                "ferc_small_power_producer_docket_no",
                "ferc_small_power_producer",
                "ferc_qualifying_facility_docket_no",
                "grid_voltage_1_kv",
                "grid_voltage_2_kv",
                "grid_voltage_3_kv",
                "iso_rto_code",
                "liquefied_natural_gas_storage",
                "natural_gas_local_distribution_company",
                "natural_gas_storage",
                "natural_gas_pipeline_name_1",
                "natural_gas_pipeline_name_2",
                "natural_gas_pipeline_name_3",
                "nerc_region",
                "net_metering",
                "pipeline_notes",
                "primary_purpose_id_naics",
                "regulatory_status_code",
                "reporting_frequency_code",
                "sector_id_eia",
                "sector_name_eia",
                "service_area",
                "transmission_distribution_owner_id",
                "transmission_distribution_owner_name",
                "transmission_distribution_owner_state",
                "utility_id_eia",
                "water_source",
                "data_maturity",
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
                    "denorm_boiler_fuel_eia923",
                    "denorm_boiler_fuel_monthly_eia923",
                    "denorm_fuel_receipts_costs_eia923",
                    "denorm_fuel_receipts_costs_monthly_eia923",
                    "denorm_generation_eia923",
                    "denorm_generation_monthly_eia923",
                    "denorm_generation_fuel_combined_eia923",
                    "denorm_generation_fuel_combined_monthly_eia923",
                    "generation_fuel_by_generator_energy_source_monthly_eia923",
                    "generation_fuel_by_generator_monthly_eia923",
                    "fuel_receipts_costs_eia923",
                    "generation_eia923",
                    "generation_fuel_eia923",
                    "generation_fuel_nuclear_eia923",
                    "heat_rate_by_unit_monthly",
                    "heat_rate_by_generator_monthly",
                    "fuel_cost_by_generator_monthly",
                    "capacity_factor_by_generator_monthly",
                    "mcoe_monthly",
                    "mcoe_generators_monthly",
                ],
            },
        },
        "field_namespace": "eia",
        "sources": ["eia860", "eia923"],
        "etl_group": "eia860",
    },
    "utilities_eia860": {
        "description": (
            "Annually varying utility attributes, compiled from all EIA data."
        ),
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
                "data_maturity",
            ],
            "primary_key": ["utility_id_eia", "report_date"],
            "foreign_key_rules": {
                "fields": [
                    ["utility_id_eia", "report_date"],
                    # Failing because this column is not harvested in the old
                    # system. TODO: re-enable when we switch to new system.
                    # https://github.com/catalyst-cooperative/pudl/issues/1196
                    # ["owner_utility_id_eia", "report_date"],
                ],
                # TODO: Excluding monthly data tables since their report_date
                # values don't match up with plants_eia860, which is annual, so
                # non-january records fail.
                # See: https://github.com/catalyst-cooperative/pudl/issues/1196
                # NOTE: EIA-861 has not gone through harvesting / normalization yet.
                "exclude": [
                    "advanced_metering_infrastructure_eia861",
                    "balancing_authority_assn_eia861",
                    "compiled_geometry_utility_eia861",
                    "demand_response_eia861",
                    "demand_response_water_heater_eia861",
                    "demand_side_management_ee_dr_eia861",
                    "demand_side_management_misc_eia861",
                    "demand_side_management_sales_eia861",
                    "denorm_boiler_fuel_eia923",
                    "denorm_boiler_fuel_monthly_eia923",
                    "denorm_fuel_receipts_costs_eia923",
                    "denorm_fuel_receipts_costs_monthly_eia923",
                    "denorm_generation_eia923",
                    "denorm_generation_monthly_eia923",
                    "denorm_generation_fuel_combined_eia923",
                    "denorm_generation_fuel_combined_monthly_eia923",
                    "fuel_cost_by_generator_monthly",
                    "generation_fuel_by_generator_energy_source_monthly_eia923",
                    "generation_fuel_by_generator_monthly_eia923",
                    # Utility IDs in this table are owners, not operators, and we are
                    # not yet harvesting owner_utility_id_eia from ownership_eia860.
                    # See https://github.com/catalyst-cooperative/pudl/issues/1393
                    "generation_fuel_by_generator_energy_source_owner_yearly_eia923",
                    "distributed_generation_fuel_eia861",
                    "distributed_generation_misc_eia861",
                    "distributed_generation_tech_eia861",
                    "distribution_systems_eia861",
                    "dynamic_pricing_eia861",
                    "energy_efficiency_eia861",
                    "fipsified_respondents_ferc714",
                    "green_pricing_eia861",
                    "mcoe_monthly",
                    "mcoe_generators_monthly",
                    "mergers_eia861",
                    "net_metering_customer_fuel_class_eia861",
                    "net_metering_misc_eia861",
                    "non_net_metering_customer_fuel_class_eia861",
                    "non_net_metering_misc_eia861",
                    "operational_data_misc_eia861",
                    "operational_data_revenue_eia861",
                    "reliability_eia861",
                    "sales_eia861",
                    "service_territory_eia861",
                    "summarized_demand_ferc714",
                    "utility_assn_eia861",
                    "utility_data_misc_eia861",
                    "utility_data_nerc_eia861",
                    "utility_data_rto_eia861",
                ],
            },
        },
        "field_namespace": "eia",
        "sources": ["eia860", "eia923"],
        "etl_group": "eia860",
    },
    "emissions_control_equipment_eia860": {
        "description": (
            """The cost, type, operating status, retirement date, and install year of
emissions control equipment reported to EIA. Includes control ids for sulfur dioxide
(SO2), particulate matter, mercury, nitrogen oxide (NOX), and acid (HCl) gas monitoring.
"""
        ),
        "schema": {
            "fields": [
                "report_year",
                "plant_id_eia",
                "emission_control_id_pudl",
                "data_maturity",
                "emission_control_equipment_type_code",
                "operational_status_code",
                "mercury_control_id_eia",
                "nox_control_id_eia",
                "particulate_control_id_eia",
                "so2_control_id_eia",
                "acid_gas_control",
                "emission_control_equipment_cost",
                "emission_control_operating_date",
                "emission_control_retirement_date",
            ],
            "primary_key": ["report_year", "plant_id_eia", "emission_control_id_pudl"],
        },
        "field_namespace": "eia",
        "sources": ["eia860"],
        "etl_group": "eia860",
    },
    "denorm_emissions_control_equipment_eia860": {
        "description": (
            """The cost, type, operating status, retirement date, and install year of
emissions control equipment reported to EIA. Includes control ids for sulfur dioxide
(SO2), particulate matter, mercury, nitrogen oxide (NOX), and acid (HCl) gas monitoring.
The denormalized version contains plant name, utility id, pudl id, and utility name
columns.
"""
        ),
        "schema": {
            "fields": [
                "report_year",
                "plant_id_eia",
                "plant_id_pudl",
                "plant_name_eia",
                "utility_id_eia",
                "utility_id_pudl",
                "utility_name_eia",
                "emission_control_id_pudl",
                "data_maturity",
                "emission_control_equipment_type_code",
                "operational_status_code",
                "operational_status",
                "mercury_control_id_eia",
                "nox_control_id_eia",
                "particulate_control_id_eia",
                "so2_control_id_eia",
                "acid_gas_control",
                "emission_control_equipment_cost",
                "emission_control_operating_date",
                "emission_control_retirement_date",
            ],
            "primary_key": ["report_year", "plant_id_eia", "emission_control_id_pudl"],
        },
        "field_namespace": "eia",
        "sources": ["eia860"],
        "etl_group": "eia860",
    },
    "boiler_emissions_control_equipment_assn_eia860": {
        "description": (
            """A table that links EIA boiler IDs to emissions control IDs for NOx, SO2,
mercury, and particulate monitoring. The relationship between the IDs is sometimes many
to many.
"""
        ),
        "schema": {
            "fields": [
                "report_date",
                "plant_id_eia",
                "boiler_id",
                "emission_control_id_type",
                "emission_control_id_eia",
                "data_maturity",
            ],
            "primary_key": [
                "report_date",
                "plant_id_eia",
                "boiler_id",
                "emission_control_id_type",
                "emission_control_id_eia",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia860"],
        "etl_group": "eia860",
    },
    "boiler_cooling_assn_eia860": {
        "description": "A table that links EIA boiler IDs to EIA cooling system IDs.",
        "schema": {
            "fields": [
                "report_date",
                "plant_id_eia",
                "boiler_id",
                "cooling_id_eia",
                "data_maturity",
            ],
            "primary_key": [
                "report_date",
                "plant_id_eia",
                "boiler_id",
                "cooling_id_eia",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia860"],
        "etl_group": "eia860",
    },
    "boiler_stack_flue_assn_eia860": {
        "description": (
            """A table that links EIA boiler IDs to EIA stack and/or flue
system IDs.
"""
        ),
        "schema": {
            "fields": [
                "report_date",
                "plant_id_eia",
                "boiler_id",
                "stack_id_eia",
                "flue_id_eia",
                "stack_flue_id_eia",
                "stack_flue_id_pudl",
            ],
            "primary_key": [
                "report_date",
                "plant_id_eia",
                "boiler_id",
                "stack_flue_id_pudl",
            ],
        },
        "field_namespace": "eia",
        "sources": ["eia860"],
        "etl_group": "eia860",
    },
}
"""EIA-860 resource attributes organized by PUDL identifier (``resource.name``).

Keys are in alphabetical order.

See :func:`pudl.metadata.helpers.build_foreign_keys` for the expected format of
``foreign_key_rules``.
"""
