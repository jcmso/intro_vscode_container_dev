import structlog

logger = structlog.get_logger(__file__)

logger.info("Hola Mundo", contexto="Inducción")

logger.info("test", contexto="test")
