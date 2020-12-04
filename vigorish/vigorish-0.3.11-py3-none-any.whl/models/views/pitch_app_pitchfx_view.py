from sqlalchemy import and_, case, func, join, or_, select
from sqlalchemy_utils import create_view

from vigorish.config.database import Base, PitchAppScrapeStatus, PitchFx


class PitchApp_PitchMix_View(Base):
    __table__ = create_view(
        name="pitch_app_pitch_mix",
        selectable=select(
            [
                PitchAppScrapeStatus.id.label("id"),
                PitchAppScrapeStatus.pitcher_id_mlb.label("pitcher_id_mlb"),
                PitchAppScrapeStatus.pitch_app_id.label("pitch_app_id"),
                PitchAppScrapeStatus.bbref_game_id.label("bbref_game_id"),
                func.count(PitchFx.id).label("total_pitches"),
                func.sum(case([(PitchFx.mlbam_pitch_name == "CH", 1)], else_=0)).label("ch_count"),
                func.sum(case([(PitchFx.mlbam_pitch_name == "CU", 1)], else_=0)).label("cu_count"),
                func.sum(case([(PitchFx.mlbam_pitch_name == "EP", 1)], else_=0)).label("ep_count"),
                func.sum(case([(PitchFx.mlbam_pitch_name == "FA", 1)], else_=0)).label("fa_count"),
                func.sum(case([(PitchFx.mlbam_pitch_name == "FC", 1)], else_=0)).label("fc_count"),
                func.sum(case([(PitchFx.mlbam_pitch_name == "FF", 1)], else_=0)).label("ff_count"),
                func.sum(case([(PitchFx.mlbam_pitch_name == "FS", 1)], else_=0)).label("fs_count"),
                func.sum(case([(PitchFx.mlbam_pitch_name == "FT", 1)], else_=0)).label("ft_count"),
                func.sum(case([(PitchFx.mlbam_pitch_name == "FO", 1)], else_=0)).label("fo_count"),
                func.sum(case([(PitchFx.mlbam_pitch_name == "IN", 1)], else_=0)).label("in_count"),
                func.sum(case([(PitchFx.mlbam_pitch_name == "KC", 1)], else_=0)).label("kc_count"),
                func.sum(case([(PitchFx.mlbam_pitch_name == "KN", 1)], else_=0)).label("kn_count"),
                func.sum(case([(PitchFx.mlbam_pitch_name == "PO", 1)], else_=0)).label("po_count"),
                func.sum(case([(PitchFx.mlbam_pitch_name == "SC", 1)], else_=0)).label("sc_count"),
                func.sum(case([(PitchFx.mlbam_pitch_name == "SI", 1)], else_=0)).label("si_count"),
                func.sum(case([(PitchFx.mlbam_pitch_name == "SL", 1)], else_=0)).label("sl_count"),
                func.sum(case([(PitchFx.mlbam_pitch_name == "UN", 1)], else_=0)).label("un_count"),
            ]
        )
        .select_from(
            join(
                PitchAppScrapeStatus,
                PitchFx,
                PitchAppScrapeStatus.id == PitchFx.pitch_app_db_id,
                isouter=True,
            )
        )
        .group_by(PitchAppScrapeStatus.id),
        metadata=Base.metadata,
        cascade_on_drop=False,
    )


class PitchApp_PitchType_View(Base):
    __table__ = create_view(
        name="pitch_app_pitch_type",
        selectable=select(
            [
                PitchAppScrapeStatus.id.label("id"),
                PitchAppScrapeStatus.pitcher_id_mlb.label("pitcher_id_mlb"),
                PitchAppScrapeStatus.pitch_app_id.label("pitch_app_id"),
                PitchAppScrapeStatus.bbref_game_id.label("bbref_game_id"),
                PitchAppScrapeStatus.season_id.label("season_id"),
                PitchFx.mlbam_pitch_name.label("pitch_type"),
                func.count(PitchFx.id).label("total_pitches"),
                func.avg(PitchFx.start_speed).label("avg_speed"),
                func.avg(PitchFx.pfx_x).label("avg_pfx_x"),
                func.avg(PitchFx.pfx_z).label("avg_pfx_z"),
                func.avg(PitchFx.px).label("avg_px"),
                func.avg(PitchFx.pz).label("avg_pz"),
            ]
        )
        .where(
            and_(
                PitchFx.is_duplicate_guid == 0,
                PitchFx.is_duplicate_pitch_number == 0,
                PitchFx.is_invalid_ibb == 0,
                PitchFx.is_out_of_sequence == 0,
                or_(PitchFx.stand == "L", PitchFx.stand == "R"),
            )
        )
        .select_from(
            join(
                PitchAppScrapeStatus,
                PitchFx,
                PitchAppScrapeStatus.id == PitchFx.pitch_app_db_id,
                isouter=True,
            )
        )
        .group_by(PitchAppScrapeStatus.id)
        .group_by(PitchFx.mlbam_pitch_name),
        metadata=Base.metadata,
        cascade_on_drop=False,
    )
