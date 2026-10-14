
import asyncio

from agents import Runner

from agent_modules.farm_planning_agent import farm_business_market_agent


def test_agent_uses_fertilizer_calculator():
    async def run_test():
        result = await Runner.run(
            farm_business_market_agent,
            """
            Calculate my fertilizer budget using these exact inputs:
            Farm area: 2 hectares
            Application rate: 200 kg per hectare
            Bag size: 50 kg
            Price per bag: 45000
            Transport cost: 10000
            Labour cost: 15000

            Use the fertilizer calculator and report the results.
            """
        )

        tool_calls = [
            item.tool_name
            for item in result.new_items
            if getattr(item, "tool_name", None) == "fertilizer_budget_tool"
        ]

        assert tool_calls, "The agent did not call the fertilizer calculator."
        assert "385000" in result.final_output.replace(",", "")

    asyncio.run(run_test())
