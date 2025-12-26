from camera import CameraResourceManager

def test_approved_case():
    manager = CameraResourceManager()
    manager.allocate_existing(3)
    assert manager.allocation_decision(4, "LOW") == "APPROVED"


def test_conditionally_approved_case():
    manager = CameraResourceManager()
    manager.allocate_existing(9)
    assert manager.allocation_decision(2, "HIGH") == "CONDITIONALLY APPROVED"


def test_rejected_case():
    manager = CameraResourceManager()
    manager.allocate_existing(8)
    assert manager.allocation_decision(5, "LOW") == "REJECTED"
