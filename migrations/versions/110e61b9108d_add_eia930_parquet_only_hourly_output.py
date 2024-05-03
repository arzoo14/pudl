"""Add eia930 parquet only hourly output

Revision ID: 110e61b9108d
Revises: e0d3904b97f4
Create Date: 2024-04-30 10:51:43.013264

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '110e61b9108d'
down_revision = 'e0d3904b97f4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('core_eia__codes_balancing_authority_subregions',
    sa.Column('balancing_authority_code_eia', sa.Text(), nullable=False, comment='EIA short code identifying a balancing authority. May include Canadian and Mexican BAs.'),
    sa.Column('balancing_authority_subregion_code_eia', sa.Enum('0001', '0004', '0006', '0027', '0035', '4001', '4002', '4003', '4004', '4005', '4006', '4007', '4008', '8910', 'ACMA', 'AE', 'AEP', 'AP', 'ATSI', 'BC', 'CE', 'COAS', 'CSWS', 'CYGA', 'DAY', 'DEOK', 'DOM', 'DPL', 'DUQ', 'EAST', 'EDE', 'EKPC', 'FREP', 'FWES', 'GRDA', 'INDN', 'JC', 'JICA', 'KACY', 'KAFB', 'KCEC', 'KCPL', 'LAC', 'LES', 'ME', 'MPS', 'NCEN', 'NPPD', 'NRTH', 'NTUA', 'OKGE', 'OPPD', 'PE', 'PEP', 'PGAE', 'PL', 'PN', 'PNM', 'PS', 'RECO', 'SCE', 'SCEN', 'SDGE', 'SECI', 'SOUT', 'SPRM', 'SPS', 'TSGT', 'VEA', 'WAUE', 'WEST', 'WFEC', 'WR', 'ZONA', 'ZONB', 'ZONC', 'ZOND', 'ZONE', 'ZONF', 'ZONG', 'ZONH', 'ZONI', 'ZONJ', 'ZONK'), nullable=False, comment='Code identifying subregions of larger balancing authorities.'),
    sa.Column('balancing_authority_subregion_name_eia', sa.Text(), nullable=True, comment='Name of the balancing authority subregion.'),
    sa.ForeignKeyConstraint(['balancing_authority_code_eia'], ['core_eia__codes_balancing_authorities.code'], name=op.f('fk_core_eia__codes_balancing_authority_subregions_balancing_authority_code_eia_core_eia__codes_balancing_authorities')),
    sa.PrimaryKeyConstraint('balancing_authority_code_eia', 'balancing_authority_subregion_code_eia', name=op.f('pk_core_eia__codes_balancing_authority_subregions'))
    )
    op.drop_table('out_ferc714__hourly_estimated_state_demand')
    op.drop_table('out_ferc714__hourly_planning_area_demand')
    op.drop_table('out_gridpathratoolkit__hourly_available_capacity_factor')
    with op.batch_alter_table('core_eia860__scd_generators_energy_storage', schema=None) as batch_op:
        batch_op.alter_column('storage_enclosure_code',
               existing_type=sa.VARCHAR(length=2),
               type_=sa.Text(),
               existing_nullable=True)
        batch_op.alter_column('storage_technology_code_1',
               existing_type=sa.VARCHAR(length=3),
               type_=sa.Text(),
               existing_nullable=True)
        batch_op.alter_column('storage_technology_code_2',
               existing_type=sa.VARCHAR(length=3),
               type_=sa.Text(),
               existing_nullable=True)
        batch_op.alter_column('storage_technology_code_3',
               existing_type=sa.VARCHAR(length=3),
               type_=sa.Text(),
               existing_nullable=True)
        batch_op.alter_column('storage_technology_code_4',
               existing_type=sa.VARCHAR(length=3),
               type_=sa.Text(),
               existing_nullable=True)

    with op.batch_alter_table('core_eia__codes_balancing_authorities', schema=None) as batch_op:
        batch_op.add_column(sa.Column('balancing_authority_region_code_eia', sa.Enum('NE', 'CAL', 'MEX', 'TEX', 'FLA', 'CAR', 'MIDA', 'SW', 'MIDW', 'CENT', 'NW', 'CAN', 'NY', 'SE'), nullable=True, comment='EIA balancing authority region code.'))
        batch_op.add_column(sa.Column('balancing_authority_region_name_eia', sa.Text(), nullable=True, comment='Human-readable name of the EIA balancing region.'))
        batch_op.add_column(sa.Column('report_timezone', sa.Enum('America/Anchorage', 'America/Chicago', 'America/Denver', 'America/Los_Angeles', 'America/New_York', 'America/Phoenix', 'Pacific/Honolulu'), nullable=True, comment='Timezone used by the reporting entity. For use in localizing UTC times.'))
        batch_op.add_column(sa.Column('balancing_authority_retirement_date', sa.Date(), nullable=True, comment='Date on which the balancing authority ceased independent operation.'))
        batch_op.add_column(sa.Column('is_generation_only', sa.Boolean(), nullable=True, comment='Indicates whether the balancing authority is generation-only, meaning it does not serve retail customers and thus reports only net generation and interchange, but not demand.'))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('core_eia__codes_balancing_authorities', schema=None) as batch_op:
        batch_op.drop_column('is_generation_only')
        batch_op.drop_column('balancing_authority_retirement_date')
        batch_op.drop_column('report_timezone')
        batch_op.drop_column('balancing_authority_region_name_eia')
        batch_op.drop_column('balancing_authority_region_code_eia')

    with op.batch_alter_table('core_eia860__scd_generators_energy_storage', schema=None) as batch_op:
        batch_op.alter_column('storage_technology_code_4',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=3),
               existing_nullable=True)
        batch_op.alter_column('storage_technology_code_3',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=3),
               existing_nullable=True)
        batch_op.alter_column('storage_technology_code_2',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=3),
               existing_nullable=True)
        batch_op.alter_column('storage_technology_code_1',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=3),
               existing_nullable=True)
        batch_op.alter_column('storage_enclosure_code',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=2),
               existing_nullable=True)

    op.create_table('out_gridpathratoolkit__hourly_available_capacity_factor',
    sa.Column('datetime_utc', sa.DATETIME(), nullable=False),
    sa.Column('aggregation_group', sa.TEXT(), nullable=False),
    sa.Column('capacity_factor', sa.FLOAT(), nullable=True),
    sa.PrimaryKeyConstraint('datetime_utc', 'aggregation_group', name='pk_out_gridpathratoolkit__hourly_available_capacity_factor')
    )
    op.create_table('out_ferc714__hourly_planning_area_demand',
    sa.Column('respondent_id_ferc714', sa.INTEGER(), nullable=False),
    sa.Column('report_date', sa.DATE(), nullable=False),
    sa.Column('datetime_utc', sa.DATETIME(), nullable=False),
    sa.Column('timezone', sa.VARCHAR(length=19), nullable=True),
    sa.Column('demand_mwh', sa.FLOAT(), nullable=True),
    sa.ForeignKeyConstraint(['respondent_id_ferc714'], ['core_ferc714__respondent_id.respondent_id_ferc714'], name='fk_out_ferc714__hourly_planning_area_demand_respondent_id_ferc714_core_ferc714__respondent_id'),
    sa.PrimaryKeyConstraint('respondent_id_ferc714', 'datetime_utc', name='pk_out_ferc714__hourly_planning_area_demand')
    )
    op.create_table('out_ferc714__hourly_estimated_state_demand',
    sa.Column('state_id_fips', sa.TEXT(), nullable=False),
    sa.Column('datetime_utc', sa.DATETIME(), nullable=False),
    sa.Column('demand_mwh', sa.FLOAT(), nullable=True),
    sa.Column('scaled_demand_mwh', sa.FLOAT(), nullable=True),
    sa.PrimaryKeyConstraint('state_id_fips', 'datetime_utc', name='pk_out_ferc714__hourly_estimated_state_demand')
    )
    op.drop_table('core_eia__codes_balancing_authority_subregions')
    # ### end Alembic commands ###
