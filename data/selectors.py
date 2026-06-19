def get_segment(data: dict, segment_id: str) -> dict:
    for segment in data["segments"]:
        if segment["id"] == segment_id:
            return segment
    raise KeyError(f"Unknown segment: {segment_id}")
