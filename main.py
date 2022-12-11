from pypresence import Presence
import time


client_id = "986699697626443888"
RPC = Presence(client_id )
RPC.connect()

while True:
    RPC.update(
        large_image="srlogo",
        large_text="SkyRegion Türkiye",
        details="Daha fazla bilgi ve eğlence için",
        state="Discord sunucumuza katılın!",
        start=int(time.time()),
        buttons= [{"label": "Site","url":"https://www.skyregiontr.com"}, {"label": "Discord","url":"https://discord.gg/bkgC89T"}]
    )
    time.sleep(999999999)