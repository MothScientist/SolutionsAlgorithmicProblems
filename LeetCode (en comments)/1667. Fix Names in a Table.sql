SELECT 
    user_id, 
    CONCAT(UPPER(substr(name, 1, 1)), LOWER(substr(name, 2))) name 
FROM 
    Users 
ORDER BY 
    user_id;