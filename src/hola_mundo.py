import structlog

logger = structlog.get_logger(__file__)

logger.info("test", contexto="tesssssst")
