from hill_set import HillSet

def main():
    hill_set = HillSet('./data/british-and-irish-hills-v-17-4.csv')
    all_hills = hill_set.get_hills()
    wainwrights = hill_set.get_wainwrights()

    hill_set.to_csv(all_hills, './data/all_hills.csv')
    hill_set.to_json(all_hills, './data/all_hills.json')

    hill_set.to_csv(wainwrights, './data/wainwrights.csv')
    hill_set.to_json(wainwrights, './data/wainwrights.json')

main()