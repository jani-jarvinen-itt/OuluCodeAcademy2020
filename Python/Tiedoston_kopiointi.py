import sys, shutil

argumenttien_määrä = len(sys.argv)
if (argumenttien_määrä < 3):
    print("Parameterejä puuttuu, anna lähde- ja kohdetiedostojen nimet.")
    exit()

lähdetiedosto = sys.argv[1]
kohdetiedosto = sys.argv[2]

print("Aloitetaan kopiointi...")
shutil.copyfile(lähdetiedosto, kohdetiedosto)
print("Kopiointi on valmis.")
