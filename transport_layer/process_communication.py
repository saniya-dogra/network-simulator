class ProcessCommunication:

    def communicate(
        self,
        source_process,
        destination_process,
        data
    ):

        print("\nPROCESS TO PROCESS COMMUNICATION")

        print(
            f"{source_process} -> {destination_process}"
        )

        print("Data :", data)