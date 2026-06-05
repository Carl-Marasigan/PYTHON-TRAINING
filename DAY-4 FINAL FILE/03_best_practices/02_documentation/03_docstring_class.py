class VideoPlayer:
    """Provides convenient functions for playing and processing video files"""

    def __init__(self, video):
        """Opens the given video to be used for later processes

        Args:
            video (str): Filename of video
        """

        self.video = video


player = VideoPlayer("test.mp4")
print(VideoPlayer)

