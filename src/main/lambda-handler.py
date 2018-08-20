# -*- coding: utf-8 -*-
#
# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not
# use this file except in compliance with the License. A copy of the License
# is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.
#

# This is a simple Hello World Alexa Skill, built using
# the decorators approach in skill builder.

# TODO: Fill these out
def takeMedicationIntent(handler_input):
    return "thanks for letting me know"

def askIfTookMedicineIntent(handler_input):
    return "yes"

TITLE = "Alexa Pillbox"

# ---------------- Intent Handling Logic ----------------- #
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_model.ui import SimpleCard

sb = SkillBuilder()

@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(handler_input):
    # Handler for Skill Launch
    speech_text = ("Welcome to the Alexa Pillbox skill!"
                    "You can tell me you took your medicine or ask me if you took your medicine already.")

    return handler_input.response_builder.speak(speech_text).set_card(
        SimpleCard(TITLE, speech_text)).set_should_end_session(
        False).response


@sb.request_handler(can_handle_func=is_intent_name("TakeMedicationIntent"))
def _intent_handler(handler_input):
    speech_text = takeMedicationIntent(handler_input)

    return handler_input.response_builder.speak(speech_text).set_card(
        SimpleCard(TITLE, speech_text)).set_should_end_session(
        True).response

@sb.request_handler(can_handle_func=is_intent_name("AskIfTookMedicineIntent"))
def _intent_handler(handler_input):
    speech_text = askIfTookMedicineIntent(handler_input)

    return handler_input.response_builder.speak(speech_text).set_card(
        SimpleCard(TITLE, speech_text)).set_should_end_session(
        True).response

@sb.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
def help_intent_handler(handler_input):
    # Handler for Help Intent
    speech_text =  "You can tell me you took your medicine or ask me if you took your medicine already."

    return handler_input.response_builder.speak(speech_text).ask(
        speech_text).set_card(SimpleCard(
            TITLE, speech_text)).response


@sb.request_handler(
    can_handle_func=lambda input:
        is_intent_name("AMAZON.CancelIntent")(input) or
        is_intent_name("AMAZON.StopIntent")(input))
def cancel_and_stop_intent_handler(handler_input):
    # Single handler for Cancel and Stop Intent
    speech_text = "Goodbye!"

    return handler_input.response_builder.speak(speech_text).set_card(
        SimpleCard(TITLE, speech_text)).response


@sb.request_handler(can_handle_func=is_intent_name("AMAZON.FallbackIntent"))
def fallback_handler(handler_input):
    # AMAZON.FallbackIntent is only available in en-US locale.
    # This handler will not be triggered except in that locale,
    # so it is safe to deploy on any locale
    speech = (
        "The " + TITLE + " skill can't help you with that.  "
        "You can tell me you took your medicine or ask me if you took your medicine already.")
    reprompt = "You can tell me you took your medicine or ask me if you took your medicine already."
    handler_input.response_builder.speak(speech).ask(reprompt)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=is_request_type("SessionEndedRequest"))
def session_ended_request_handler(handler_input):
    # Handler for Session End
    return handler_input.response_builder.response


@sb.exception_handler(can_handle_func=lambda i, e: True)
def all_exception_handler(handler_input, exception):
    # Catch all exception handler, log exception and
    # respond with custom message
    print("Encountered following exception: {}".format(exception))

    speech = "Sorry, there was some problem. Please try again!!"
    handler_input.response_builder.speak(speech).ask(speech)

    return handler_input.response_builder.response

handler = sb.lambda_handler()
