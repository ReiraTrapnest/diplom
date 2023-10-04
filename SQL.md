### Проверить, отображается ли созданный заказ в базе данных

SELECT c.login, COUNT (o."inDelivery") AS "Active orders",
FROM JOIN "Orders" AS o ON c.id = o."courierId"
WHERE o."inDelivery" = true,
GROUP BY c.login

### Убедиться, что в базе данных статусы заказов записываются корректно

SELECT track
CASE
    WHEN finished = TRUE THEN 2
    WHEN canсelled = TRUE THEN -1
    WHEN inDelivery = TRUE THEN 1
    ELSE 0
END AS status
FROM "Orders"