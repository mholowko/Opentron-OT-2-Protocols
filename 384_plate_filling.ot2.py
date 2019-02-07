from opentrons import instruments, labware

metadata = {
    'protocolName': 'Plate Filling',
    'author': 'Maciej Holowko <maciej.holowko@csiro.au>',
    }

#trough = labware.create(
#        '12_well_through_lp',                    # name of you labware
#        grid=(1, 12),                    # specify amount of (columns, rows)
#        spacing=(1, 14),               # distances (mm) between each (column, row)
#        diameter=7,                     # diameter (mm) of each well on the plate
#        depth=10,                       # depth (mm) of each well on the plate
#        volume=2000)


# trough and 384-well plate
trough = labware.load('12_well_through_lp', '3', 'trough')
plate = labware.load('384-plate', '2', 'plate')

# 8-channel 10uL pipette, with tip rack and trash
tiprack = labware.load('tiprack-200ul', '1', 'p200rack')

pipette = instruments.P300_Multi(mount='left',tip_racks=[tiprack])

alternating_wells = []
for column in plate.cols():
    alternating_wells.append(column.wells('A', length=8, step=2))
    alternating_wells.append(column.wells('B', length=8, step=2))
        
pipette.distribute(3.8, trough.wells('A1'), alternating_wells,trash=False)


