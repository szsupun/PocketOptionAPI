"""
Get Payout Information from PocketOption API

This script demonstrates how to retrieve payout information for assets.
Payout data is automatically received from the server when connected.
"""

import asyncio
from pocketoptionapi_async import AsyncPocketOptionClient


async def main():
    # Get SSID from user
    SSID = input("Enter your SSID: ")

    # Create client
    client = AsyncPocketOptionClient(SSID, is_demo=True, enable_logging=True)

    # Connect to PocketOption
    print("Connecting to PocketOption...")
    await client.connect()

    print("Waiting for payout data (this may take a few seconds)...")
    
    # Wait for payouts to be received (timeout after 15 seconds)
    payouts = await client.wait_for_payouts(timeout=15.0)

    if payouts:
        print(f"\n✅ Received payout data for {len(payouts)} assets:")
        print("\n" + "=" * 60)
        
        # Display all payouts in the format requested by user
        for symbol, payout_info in sorted(payouts.items()):
            payout_data = {
                "id": payout_info.get("id"),
                "symbol": payout_info.get("symbol"),
                "name": payout_info.get("name"),
                "type": payout_info.get("type"),
                "payout": payout_info.get("payout"),
            }
            print(f"\n{payout_data}")
        
        print("\n" + "=" * 60)
        
        # Example: Get payout for a specific asset
        example_symbol = list(payouts.keys())[0] if payouts else None
        if example_symbol:
            specific_payout = client.get_payouts(symbol=example_symbol)
            print(f"\n📌 Example: Getting payout for {example_symbol}:")
            print(f"   {specific_payout}")
    else:
        print("\n⚠️ No payout data received yet. The server may not have sent payout updates.")
        print("   Try waiting a bit longer or check your connection.")

    # Keep connection alive for a bit to receive more updates
    print("\nKeeping connection alive for 10 seconds to receive more updates...")
    await asyncio.sleep(10)

    # Disconnect
    await client.disconnect()
    print("\nDisconnected.")


if __name__ == "__main__":
    asyncio.run(main())


