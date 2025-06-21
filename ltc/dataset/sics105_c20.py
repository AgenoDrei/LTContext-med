from ltc.dataset.video_dataset import VideoDataset
import ltc.utils.logging as logging

logger = logging.get_logger(__name__)


class sics105_c20(VideoDataset):
    def __init__(self, cfg, mode):
        super(sics105_c20, self).__init__(cfg, mode)
        logger.info("Constructing SICS-105 (c20) {} dataset with {} videos.".format(mode, self._dataset_size))
