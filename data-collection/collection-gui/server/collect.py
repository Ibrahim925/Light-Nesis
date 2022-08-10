import time
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
from brainflow.data_filter import DataFilter
import os

# Parameters for data saving
ext = ".csv"
sfreq = 200 #Ganglion sampling rate

def collect_data(sex, participant, direction, run):
    BoardShim.enable_dev_board_logger()

    # Arguments for board
    params = BrainFlowInputParams()
    params.serial_port = "/dev/cu.usbmodem11"

    # Make connection to board
    try:    
        board = BoardShim(BoardIds.GANGLION_BOARD, params)
        board.prepare_session()
        board.start_stream()
        time.sleep(27)
        data = board.get_board_data()  # get all data and remove it from internal buffer
        board.stop_stream()
        board.release_session()
        dir_path = os.path.join("..", "..", "..", "data", sex, participant, direction)
        file_path = os.path.join(dir_path, run + ext)

        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        DataFilter.write_file(data, file_path, "w")
        
    except:
        raise Exception("Unable to connect to the Ganglion Board :(")

    
