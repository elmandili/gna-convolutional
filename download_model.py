import asyncio
import skillsnetwork

async def download():
    generator_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML311-Coursera/labs/Module6/generator.tar.gz"
    await skillsnetwork.prepare(generator_url, overwrite=True)
    print("Download complete!")

asyncio.run(download())