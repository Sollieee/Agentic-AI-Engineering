
import asyncio

from agents import Runner

from agent_modules.orchestrator import agriassist_agent
from test_routing import get_called_tools


def run_routing_test(prompt, expected_specialist):
    async def run_test():
        result = await Runner.run(agriassist_agent, prompt)
        called_tools = get_called_tools(result.new_items)

        print(f"\nUser prompt: {prompt}")
        print(f"Expected specialist: {expected_specialist}")
        print(f"Specialists called: {called_tools}")

        assert expected_specialist in called_tools, (
            f"Expected {expected_specialist}, "
            f"but the tools called were: {called_tools}"
        )

    asyncio.run(run_test())


def test_indirect_maize_planting_question():
    run_routing_test(
        "The rains have started here, and I'm thinking of planting "
        "maize on my land. What should I be doing first?",
        "farming_advisor",
    )


def test_vague_yellow_maize_leaves():
    run_routing_test(
        "My maize was looking fine before, but now some leaves "
        "are turning yellow. I don't know what's happening.",
        "crop_health_specialist",
    )


def test_natural_language_farm_budget_question():
    run_routing_test(
        "I have one hectare of land and want to start maize farming, "
        "but I don't know how much money I should put aside.",
        "farm_business_market_specialist",
    )


def test_ambiguous_crop_problem():
    async def run_test():
        prompt = (
            "My crops aren't doing well, and I'm not sure what's "
            "wrong. Can you help me figure out where to start?"
        )

        result = await Runner.run(agriassist_agent, prompt)
        called_tools = get_called_tools(result.new_items)

        print(f"\nUser prompt: {prompt}")
        print(f"Specialists called: {called_tools}")
        print(f"AgriAssist response: {result.final_output}")

        # An ambiguous request does not have to trigger a specialist.
        # If one is called, it should be relevant to the problem.
        relevant_specialists = {
            "farming_advisor",
            "crop_health_specialist",
        }

        assert set(called_tools).issubset(relevant_specialists), (
            f"Unexpected specialist calls: {called_tools}"
        )

    asyncio.run(run_test())



def test_combined_crop_health_and_fertilizer_budget():
    async def run_test():
        prompt = (
            "My maize leaves are turning yellow, and I also need "
            "to work out how much fertilizer I should budget for "
            "the next planting season."
        )

        result = await Runner.run(agriassist_agent, prompt)
        called_tools = get_called_tools(result.new_items)

        print(f"\nUser prompt: {prompt}")
        print(f"Specialists called: {called_tools}")
        print(f"AgriAssist response: {result.final_output}")

        expected_specialists = {
            "crop_health_specialist",
            "farm_business_market_specialist",
        }

        missing_specialists = expected_specialists - set(called_tools)

        assert not missing_specialists, (
            f"Expected specialists were not called: "
            f"{missing_specialists}. "
            f"Actual calls: {called_tools}"
        )

    asyncio.run(run_test())


def test_weak_chickens_and_reduced_appetite():
    async def run_test():
        prompt = (
            "My chickens haven't been eating properly since yesterday, "
            "and a few look weak. What do you think I should do?"
        )

        result = await Runner.run(agriassist_agent, prompt)
        called_tools = get_called_tools(result.new_items)

        print(f"\nUser prompt: {prompt}")
        print(f"Specialists called: {called_tools}")
        print(f"AgriAssist response: {result.final_output}")

        assert "livestock_specialist" in called_tools, (
            f"Expected livestock_specialist to be called, "
            f"but the tools called were: {called_tools}"
        )

    asyncio.run(run_test())


def test_unresolved_poultry_feed_delivery():
    async def run_test():
        prompt = (
            "I ordered poultry feed last week, but it still hasn't "
            "arrived. I've tried contacting the supplier, but "
            "I haven't received a clear response. What should I do next?"
        )

        result = await Runner.run(agriassist_agent, prompt)
        called_tools = get_called_tools(result.new_items)

        print(f"\nUser prompt: {prompt}")
        print(f"Specialists called: {called_tools}")
        print(f"AgriAssist response: {result.final_output}")

        assert "agricultural_support_specialist" in called_tools, (
            f"Expected agricultural_support_specialist to be called, "
            f"but the tools called were: {called_tools}"
        )

    asyncio.run(run_test())
