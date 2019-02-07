from opentrons import instruments, labware

metadata = {
    'protocolName': 'Plate Filling',
    'author': 'Maciej Holowko <maciej.holowko@csiro.au>',
    }

# trough and 384-well plate
#trough = labware.create(
#        '4_well_through',                    # name of you labware
#        grid=(1, 4),                    # specify amount of (columns, rows)
#        spacing=(1, 50),               # distances (mm) between each (column, row)
#        diameter=25,                     # diameter (mm) of each well on the plate
#        depth=30,                       # depth (mm) of each well on the plate
#        volume=20000)

trough = labware.load('4_well_through','3','trough')
plate = labware.load('96-PCR-flat', '2', 'plate')

tiprack = labware.load('tiprack-200ul', '1', 'p200rack')

pipette = instruments.P300_Multi(mount='left',tip_racks=[tiprack])

pipette.distribute(200, trough.wells('A1'), plate.cols(0,length=12),trash=False)
