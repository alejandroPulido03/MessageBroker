sudo docker run -it --rm --name rabbitmq -d -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management &&
sudo docker run --name postgres-offers-db -e POSTGRES_USER=los_full_stack_overflow -e POSTGRES_PASSWORD=los_full_stack_underflow -e POSTGRES_DB=offers_service -d postgres
