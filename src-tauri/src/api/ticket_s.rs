use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize, Debug)]
pub struct Task{
    id: i32,
    agent_id: i32,
    status: String,
    due_date: String,
    notify_before: String,
    title: String,
    description: String,
    created_at: String,
    updated_at: String,
    closed_at: String,
    group_id: i32,
    deleted: bool,
    custom_fields: Vec<String>,
    workspace_id: i32
}

#[derive(Serialize, Deserialize, Debug)]
pub struct TicketInfo{
    cc_emails: Vec<String>,
    fwd_emails: Vec<String>,
    reply_cc_emails: Vec<String>,
    bcc_emails: Vec<String>,
    fr_escalated: bool,
    spam: bool,
    email_config_id: i32,
    group_id: i32,
    priority: i32,
    requester_id: i32,
    requested_for_id: i32,
    responder_id: i32,
    source: i32,
    status: i32,
    subject: String,
    to_emails: Vec<String>,
    sla_policy_id: i32,
    applied_business_hours: i32,
    department_id: i32,
    id: i32,
    type_: String,
    due_by: String,
    fr_due_by: String,
    is_escalated: bool,
    description: String,
    description_text: String,
    custom_fields: Vec<String>,
    created_at: String,
    updated_at: String,
    urgency: i32,
    impact: i32,
    category: String,
    sub_category: String,
    item_category: String,
    deleted: bool,
    attachments: Vec<String>,
    workspace_id: i32,
    created_within_business_hours: bool,
}

#[derive(Serialize, Deserialize, Debug)]
pub struct Ticket{
    ticket: TicketInfo,
}