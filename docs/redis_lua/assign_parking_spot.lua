local plane_id = KEYS[1]
redis.replicate_commands()

if tonumber(plane_id) > 80 or tonumber(plane_id) < 1 then
  return "plane_id not in range"
end

if redis.call("EXISTS", "available_parking_spots") == 0 then
  for i=1,99 do
    redis.call("SADD", "available_parking_spots", i)
  end
end


if redis.call("EXISTS", plane_id) == 1 then
  return redis.call("GET", plane_id)
else
  local parking_id = redis.call("SPOP", "available_parking_spots")
  redis.call("SET", plane_id, parking_id)
  return parking_id
end