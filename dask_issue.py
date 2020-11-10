from src.network import Network
from dask.distributed import Client

if __name__ == '__main__':

    client = Client()

    xor_net = Network(name="xor")
    xor_net.add_group(name="first", num_units=2, group_type="input", input_transforms=[], output_transforms=[])
    xor_net.add_group(name="second", num_units=2, group_type="hidden", input_transforms=["dot"], output_transforms=["sigmoid"])
    xor_net.add_group(name="third", num_units=1, group_type="output", input_transforms=["dot"], output_transforms=["sigmoid"])

    print(xor_net.print_name())
    print(client.submit(xor_net.print_name).result())

