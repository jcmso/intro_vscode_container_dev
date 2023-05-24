import structlog

logger = structlog.get_logger(__file__)

logger.info("Hola Jorge", contexto="Inducción")