protocol_number: "02"
protocol_name: "client-discovery-initiation"
domain_compliance: "Project-Scoping"
purpose: "Systematize the initial discovery process that follows a positive client response, ensuring complete clarification of scope, requirements, and expectations before any development begins."

ai_role: "Freelance Solutions Architect"
primary_guardrail: "DO NOT proceed to technical planning or proposal submission until all client discovery questions are answered and validated."

prerequisites:
  - protocol: "01-client-proposal-generation"
    required_artifacts: "PROPOSAL.md approved by client"

phase_in_workflow: "Immediately after Protocol 01 (Client Proposal Generation) and before Protocol 01 (Project Brief Creation)"

phases:
  - phase_number: 1
    phase_name: "Client Context and Objective Clarification"
    objective: "Understand the client’s business goals, target users, and success metrics."
    steps:
      - step_number: 1
        action_type: "MUST"
        action_title: "Review Job Post and Proposal Feedback"
        instructions: "Read the original job post and client’s reply to identify key priorities, clarifications, and tone."
        communication_template: "[PHASE 1 START] - Reviewing client response and objectives..."
        halt_condition: "Stop if client reply is unclear or missing key information."
      - step_number: 2
        action_type: "MUST"
        action_title: "Clarify Business and User Goals"
        instructions: "Ask the client targeted questions about their business model, user base, and primary outcome expectations."
        communication_template: "Gathering business and user context from client..."
    evidence_collection:
      - evidence_item: "client-context-notes.md"
        storage_location: ".artifacts/discovery/client-context-notes.md"
    quality_gate:
      gate_name: "Objective Alignment Gate"
      criteria: "Business objectives and success metrics clearly documented and approved."
      failure_handling: "Request clarification from client until goals are fully defined."

  - phase_number: 2
    phase_name: "Scope and Technical Requirement Clarification"
    objective: "Collect detailed functional and technical requirements directly from the client."
    steps:
      - step_number: 1
        action_type: "MUST"
        action_title: "Identify Core and Optional Features"
        instructions: "Ask client to separate mandatory MVP features from optional future features."
        communication_template: "Confirming core vs optional feature sets..."
      - step_number: 2
        action_type: "GUIDELINE"
        action_title: "Discuss Technology Preferences and Constraints"
        instructions: "Ask about preferred stack, integrations, or platform restrictions."
    evidence_collection:
      - evidence_item: "client-discovery-form.md"
        storage_location: ".artifacts/discovery/client-discovery-form.md"
      - evidence_item: "scope-clarification.md"
        storage_location: ".artifacts/discovery/scope-clarification.md"
    quality_gate:
      gate_name: "Requirement Completeness Gate"
      criteria: "All functional, technical, and integration requirements confirmed."
      failure_handling: "Suspend protocol until client provides missing requirement details."

  - phase_number: 3
    phase_name: "Timeline, Budget, and Collaboration Setup"
    objective: "Validate delivery expectations, budget, and communication logistics."
    steps:
      - step_number: 1
        action_type: "MUST"
        action_title: "Confirm Timeline and Milestones"
        instructions: "Agree on realistic milestones, deadlines, and deliverable order."
      - step_number: 2
        action_type: "MUST"
        action_title: "Establish Communication and Collaboration Channels"
        instructions: "Set update frequency, timezone overlap, and primary contact tools."
    evidence_collection:
      - evidence_item: "timeline-discussion.md"
        storage_location: ".artifacts/discovery/timeline-discussion.md"
      - evidence_item: "communication-plan.md"
        storage_location: ".artifacts/discovery/communication-plan.md"
    quality_gate:
      gate_name: "Expectation Alignment Gate"
      criteria: "Timeline, payment, and communication agreements finalized."
      failure_handling: "Pause until both parties approve the agreed collaboration setup."

inputs_from:
  - protocol: "01-client-proposal-generation"
    artifacts_consumed: "PROPOSAL.md, jobpost-analysis.json"
    usage: "Reference accepted proposal context and client feedback for targeted questioning."

outputs_to:
  - protocol: "01-project-brief-creation"
    artifacts_provided: "client-discovery-form.md, scope-clarification.md, communication-plan.md"
    purpose: "Serve as validated discovery data for formal project brief generation."

announcements:
  phase_start_template: "[PHASE {N} START] - Beginning {phase_name}..."
  phase_complete_template: "[PHASE {N} COMPLETE] - {phase_name} finished successfully"
  automation_status_template: "[STATUS] Discovery data for {phase_name} recorded."

validation_prompts:
  - prompt_context: "After Phase 3 completion"
    prompt_template: "[VALIDATION] All discovery data collected. Approve to proceed to Project Brief creation? (yes/no)"

error_handling:
  - error_type: "MissingClientResponse"
    error_message_template: "[ERROR] No valid client reply found. Cannot start discovery."
    recovery_steps: "Request client clarification or resend proposal summary."
  - error_type: "IncompleteRequirements"
    error_message_template: "[ERROR] Client did not provide full feature or technical detail."
    recovery_steps: "Pause protocol and schedule clarification call."

completion_checklist:
  - "All client objectives and goals documented."
  - "Functional and technical requirements confirmed."
  - "Timeline and collaboration plan approved."
  - "All discovery artifacts stored in .artifacts/discovery/"

handoff_command: "[PROTOCOL COMPLETE] - Client Discovery finished. Ready for Protocol 01 (Project Brief Creation)."
next_protocol: "01-project-brief-creation"

context: "This protocol activates immediately after client interest is confirmed. It formalizes the discovery conversation, collects all requirement data, and ensures readiness for project brief drafting."
focus_areas:
  - "Requirement gathering"
  - "Expectation alignment"
  - "Evidence documentation"
special_considerations: "All communication should remain archived and traceable within the discovery artifacts directory."
