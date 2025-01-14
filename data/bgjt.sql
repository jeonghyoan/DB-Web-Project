SELECT * FROM testdb.articles4;

-- 광고글 제거, 사이트 이름 번개장터로 변경
delete from articles4 where published_at='AD';
update articles4 set site_name='번개장터';

-- 최종테이블에서 price 자료형을 int로 바꾸기 위해 price값에서 ',' 제거
update articles4 set price =replace(price,',','');

-- published_at_mod 컬럼 만든 후 crawled_at 값 복사해 넣기
-- published_at값을 시간형식으로 변경 (ex>5초전-> 00:00:05)
-- published_at_mod값(crawled_at 값)에서 published_at값을 빼서 게시글 작성 시간 구하기
alter table articles4 add published_at_mod varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL after published_at;
update articles4 set published_at_mod=crawled_at;

-- 몇초 전, 몇분 전, 몇시간 전, 며칠전, 몇주 전 시간 형식으로 변환
-- 초
update articles4 set published_at=substring_index(published_at,"초",1) where published_at like'%초%';
update articles4 set published_at=str_to_date(published_at,'%s') WHERE published_at REGEXP '^[0-9]+$';
update articles4 set published_at_mod=subtime(published_at_mod,published_at) where published_at like '%:%';
update articles4 set published_at='초' where published_at like '%:%';

-- 분
update articles4 set published_at=substring_index(published_at,"분",1) where published_at like'%분%';
update articles4 set published_at=str_to_date(published_at,'%i') WHERE published_at REGEXP '^[0-9]+$';
update articles4 set published_at_mod=subtime(published_at_mod,published_at) where published_at like '%:%';
update articles4 set published_at='분' where published_at like '%:%';

-- 시간
update articles4 set published_at=substring_index(published_at,"시간",1) where published_at like'%시간%';
update articles4 set published_at=str_to_date(published_at,'%H') WHERE published_at REGEXP '^[0-9]+$';
update articles4 set published_at_mod=subtime(published_at_mod,published_at) where published_at like '%:%';
update articles4 set published_at='시간' where published_at like '%:%';


-- 일
update articles4 set published_at=substring_index(published_at,"일",1) where published_at like'%일%';
update articles4 set published_at=str_to_date(published_at,'%d') WHERE published_at REGEXP '^[0-9]+$';
update articles4 set published_at=str_to_date(published_at,'%Y-%m-%d %H:%i:%s') where published_at like '%-%';
update articles4 set published_at_mod=date_sub(published_at_mod, Interval day(published_at) day) where published_at like '%-%';
update articles4 set published_at='일' where published_at like '%-%';


-- 주
update articles4 set published_at=substring_index(published_at,"주",1) where published_at like'%주%';
update articles4 set published_at=str_to_date(published_at,'%d') WHERE published_at REGEXP '^[0-9]+$';
update articles4 set published_at=str_to_date(published_at,'%Y-%m-%d %H:%i:%s') where published_at like '%-%';
update articles4 set published_at_mod=date_sub(published_at_mod, Interval 7*day(published_at) day) where published_at like '%-%';

-- published_at 컬럼 삭제후, 게시글 작성 시간인 published_at_mod를 published_at으로 변경
alter table articles4 drop published_at;
alter table articles4 change published_at_mod published_at varchar(45);
