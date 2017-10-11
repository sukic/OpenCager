-- with ZIP CODE
SELECT 
       --row_number() OVER (PARTITION BY 1) id,
       src_id,
       CASE WHEN objekt IS NOT NULL AND adresa IS NOT NULL AND ulice IS NOT NULL THEN  psc_string||','||ulice||' '||objekt||'/'||adresa||','||obec_orig
            WHEN objekt IS NOT NULL AND adresa IS NULL AND ulice IS NOT NULL THEN psc_string||','||ulice||' '||objekt||','||obec_orig
            WHEN objekt IS NULL AND adresa IS NOT NULL AND ulice IS NOT NULL THEN psc_string||','||ulice||' '||adresa||','||obec_orig
            WHEN objekt IS NOT NULL AND adresa IS NOT NULL AND ulice IS NULL THEN psc_string||','||objekt||'/'||adresa||','||obec_orig
            WHEN objekt IS NOT NULL AND adresa IS NULL AND ulice IS NULL THEN psc_string||','||objekt||','||obec_orig
            WHEN objekt IS NULL AND adresa IS NOT NULL AND ulice IS NULL THEN psc_string||','||adresa||','||obec_orig
            WHEN objekt IS NULL AND adresa IS NULL AND ulice IS NOT NULL THEN psc_string||','||ulice||','||obec_orig
       END address
   FROM vzorek
     WHERE obec_orig IS NOT NULL AND
           psc_string IS NOT NULL
   ORDER BY random();

-- without ZIP CODE
SELECT 
       --row_number() OVER (PARTITION BY 1) id,
       src_id,
       CASE WHEN objekt IS NOT NULL AND adresa IS NOT NULL AND ulice IS NOT NULL THEN  ulice||' '||objekt||'/'||adresa||','||obec_orig
            WHEN objekt IS NOT NULL AND adresa IS NULL AND ulice IS NOT NULL THEN ulice||' '||objekt||','||obec_orig
            WHEN objekt IS NULL AND adresa IS NOT NULL AND ulice IS NOT NULL THEN ulice||' '||adresa||','||obec_orig
            WHEN objekt IS NOT NULL AND adresa IS NOT NULL AND ulice IS NULL THEN objekt||'/'||adresa||','||obec_orig
            WHEN objekt IS NOT NULL AND adresa IS NULL AND ulice IS NULL THEN objekt||','||obec_orig
            WHEN objekt IS NULL AND adresa IS NOT NULL AND ulice IS NULL THEN adresa||','||obec_orig
            WHEN objekt IS NULL AND adresa IS NULL AND ulice IS NOT NULL THEN ulice||','||obec_orig
       END address
   FROM vzorek
     WHERE obec_orig IS NOT NULL
           
   ORDER BY random();
