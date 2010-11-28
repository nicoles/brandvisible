insert into companies_company select cw_id, company_name, cik from cw.companies;
insert into companies_company_parent select relation_id, source_cw_id, target_cw_id from cw.company_relations group by source_cw_id, target_cw_id;
insert into companies_company_top_parent (from_company_id, to_company_id) select cw_id, top_parent_id from cw.company_info where cw_id != top_parent_id group by cw_id;
insert into companies_company_top_parent_of (from_company_id, to_company_id) select top_parent_id, cw_id from cw.company_info where cw_id != top_parent_id group by cw_id;
