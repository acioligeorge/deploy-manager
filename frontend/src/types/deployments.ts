export interface Deployment {
    id: string
    name: string
    status: "running" | "stopped" | "error"
    created_at: string
}