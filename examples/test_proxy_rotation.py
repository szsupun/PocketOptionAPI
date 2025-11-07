"""
Example: Test Proxy Rotation

This example demonstrates how to use multiple proxies with automatic rotation.
Use free proxies from testing sites to test before buying.
"""

import asyncio
from pocketoptionapi_async import AsyncPocketOptionClient


async def main():
    ssid = input("Enter your SSID: ").strip()
    if not ssid:
        print("SSID is required")
        return

    # Example: Multiple proxies for rotation
    # Replace with your actual proxy list
    print("\nEnter proxy URLs (one per line, empty line to finish):")
    proxies = []
    while True:
        proxy = input("Proxy URL (or press Enter to finish): ").strip()
        if not proxy:
            break
        proxies.append(proxy)
    
    if not proxies:
        print("No proxies provided. Using direct connection.")
        proxies = None
    else:
        print(f"\nUsing {len(proxies)} proxies with rotation")

    # Create client with proxy rotation
    client = AsyncPocketOptionClient(
        ssid,
        is_demo=True,
        enable_logging=True,
        proxy=proxies,  # Can be single string or list
        proxy_rotation=True  # Enable rotation
    )

    connected = await client.connect()
    if not connected:
        print("Failed to connect")
        return

    print("\nConnected successfully!")
    print("Proxy rotation is active - each reconnection will use a different proxy")

    # Wait for payouts
    payouts = await client.wait_for_payouts(timeout=15.0)

    if payouts:
        print(f"\nReceived {len(payouts)} payouts")
        # Show first 3
        for i, (symbol, info) in enumerate(sorted(payouts.items())[:3], 1):
            payout_info = {
                "id": info.get("id"),
                "symbol": info.get("symbol"),
                "name": info.get("name"),
                "type": info.get("type"),
                "payout": info.get("payout"),
            }
            print(f"{i}. {payout_info}")
    else:
        print("No payout data received")

    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())

