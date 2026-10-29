import os
os.environ["PMIX_HOSTNAME"] = "localhost"


from mpi4py import MPI
import sys

print(MPI.Get_library_version())

comm = MPI.COMM_SELF.Spawn(
    sys.executable,
    args=["-c", "pass"],
    maxprocs=1,
)

comm.Disconnect()