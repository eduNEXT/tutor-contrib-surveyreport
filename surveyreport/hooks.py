from tutor.types import Config, get_typed
from tutor import hooks, config as tutor_config, fmt
import click
from tutor.interactive import ask_bool


@hooks.Actions.INTERACTIVE_CONFIGURATION.add()
def ask_survey_report_questions(config: Config) -> None:
    defaults = tutor_config.get_defaults()
    enable_survey_report = click.confirm(
        fmt.question(
            "Would you like to send reports of usage back to the Open edX project?"
            " Type 'n' if you don't want to"
        ),
        prompt_suffix=" ",
        default=True,
    )
    config["SURVEYREPORT_ENABLE"] = enable_survey_report

    if enable_survey_report:
        ask_bool(
            (
                "Send anonymous survey report? Important note:"
                " the report will be sent with a unique id instead of site name."
            ),
            "SURVEYREPORT_ANONYMOUS",
            config,
            defaults,
        )
        ask_bool(
            (
                "Send survey report automatically? Important note:"
                " If you don't want to send it automatically, you must send it from Django admin."
            ),
            "SURVEYREPORT_AUTO_SEND",
            config,
            defaults,
        )
        