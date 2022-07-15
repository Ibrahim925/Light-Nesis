import argparse
import time
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
from brainflow.data_filter import DataFilter
import os

# Parameters for data collection
sex = ["male", "female"][0]
participant = "01"
direction = ["left", "none", "right"][0]
run = "01"
ext = ".csv"

if not os.path.exists(os.path.join("data", sex, participant, direction)):
    os.makedirs(os.path.join("data", sex, participant, direction))

def main():
    def collect_data():
        BoardShim.enable_dev_board_logger()

        # Arguments for board
        parser = argparse.ArgumentParser()
        parser.add_argument('--serial-port', type=str, help='serial port', required=False, default='/dev/cu.usbmodem11')
        parser.add_argument('--board-id', type=int, help='board id, check docs to get a list of supported boards', required=False, default=BoardIds.GANGLION_BOARD)
        args = parser.parse_args()
        params = BrainFlowInputParams()
        params.serial_port = args.serial_port

        
        board = BoardShim(args.board_id, params)
        board.prepare_session()
        board.start_stream()
        time.sleep(27)
        data = board.get_board_data()  # get all data and remove it from internal buffer
        board.stop_stream()
        board.release_session()

        DataFilter.write_file(data, os.path.join("data", sex, participant, direction, run + ext), "w")

    collect_data()

if __name__ == "__main__":
    main()
