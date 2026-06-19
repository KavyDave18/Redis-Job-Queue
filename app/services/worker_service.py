import asyncio
from app.services.queue_service import update_job_status,save_job_result

async def process_job(
    job_id: str,
    task: str
):

    try:

        await update_job_status(
            job_id,
            "PROCESSING"
        )

        print(
            f"Processing: {task}"
        )

        await asyncio.sleep(10)

        if task == "fail":

            raise Exception(
                "Simulated Failure"
            )

        result = (
            f"Task '{task}' completed successfully"
        )

        await save_job_result(
            job_id,
            result
        )

        await update_job_status(
            job_id,
            "COMPLETED"
        )

    except Exception as e:

        await save_job_result(
            job_id,
            str(e)
        )

        await update_job_status(
            job_id,
            "FAILED"
        )

        print(
            f"Failed: {task}"
        )