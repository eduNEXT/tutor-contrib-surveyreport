from tutor.types import Config, get_typed
from tutor import hooks, config as tutor_config, fmt
import click
from tutor.interactive import ask_bool

@hooks.Actions.CONFIG_INTERACTIVE.add()
def ask_survey_report_questions(config: Config) -> None:
    fmt.echo_info(
    """The Open edX Project relies on the collective strength of its community to be a thriving platform for online education"""
    )
    fmt.echo_info(
    """We invite you to join the Open edX Data Sharing Initiative by sharing an anonymized reports of aggregated data from your institution's usage of the platform."""
    )
    fmt.echo_info(
    """The report data will be sent to Axim Collaborative, the non-profit behind the Open edX project."""
    )

    texto_con_enlace = click.style("See more: https://github.com/eduNEXT/edx-platform/tree/master/openedx/features/survey_report#survey-report", fg='blue', underline=True)
    click.echo(texto_con_enlace)

    defaults = tutor_config.get_defaults()
    enable_survey_report = click.confirm(
        fmt.question(
            "Would you like to send automatic and anonymized reports of usage back to the Open edX project?"
            " Type 'n' if you don't want to"
        ),
        prompt_suffix=" ",
        default=True,
    )
    config["SURVEYREPORT_ENABLE"] = enable_survey_report
    config["SURVEYREPORT_AUTO_SEND"] = enable_survey_report
