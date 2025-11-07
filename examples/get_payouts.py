"""
Minimal example: fetch payouts and print one asset's payout info.
Run: python examples/get_payouts.py
"""

import asyncio
from pocketoptionapi_async import AsyncPocketOptionClient


async def main():
    ssid = input("Enter your SSID: ").strip()
    if not ssid:
        print("SSID is required")
        return

    client = AsyncPocketOptionClient(ssid, is_demo=True, enable_logging=False)

    connected = await client.connect()
    if not connected:
        print("Failed to connect")
        return

    # Wait a bit for payouts to arrive
    payouts = await client.wait_for_payouts(timeout=15.0)

    if not payouts:
        print("No payout data received.")
        await client.disconnect()
        return

    # Ask for a symbol to lookup (e.g., #EURUSD, #AAPL, BTCUSD, etc.)
    symbol = input("Enter asset symbol (e.g., #EURUSD) or press Enter to list first 5: ").strip()

    if symbol:
        info = client.get_payouts(symbol=symbol)
        if info:
            payout_info = {
                "id": info.get("id"),
                "symbol": info.get("symbol"),
                "name": info.get("name"),
                "type": info.get("type"),
                "payout": info.get("payout"),
            }
            print(payout_info)
        else:
            print(f"No payout data found for {symbol}")
    else:
        # Print a few examples
        count = 0
        for _, info in sorted(payouts.items()):
            payout_info = {
                "id": info.get("id"),
                "symbol": info.get("symbol"),
                "name": info.get("name"),
                "type": info.get("type"),
                "payout": info.get("payout"),
            }
            print(payout_info)
            count += 1
            if count >= 5:
                break

    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())


