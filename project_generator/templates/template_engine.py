"""
Template Engine for generating code templates
"""

from typing import Dict, Any


class TemplateEngine:
    """Generates code templates for different frameworks and industries"""
    
    def generate_page_template(self, page_name: str, frontend: str, industry: str) -> str:
        """Generate a frontend page template"""
        templates = {
            'nextjs': self._nextjs_page_template,
            'nuxt': self._nuxt_page_template,
            'angular': self._angular_page_template,
            'expo': self._expo_page_template
        }
        
        generator = templates.get(frontend)
        if generator:
            return generator(page_name, industry)
        
        return f"// {page_name} page template for {frontend}"
    
    def generate_api_template(self, api_name: str, backend: str, industry: str) -> str:
        """Generate a backend API template"""
        templates = {
            'fastapi': self._fastapi_api_template,
            'django': self._django_api_template,
            'nestjs': self._nestjs_api_template,
            'go': self._go_api_template
        }
        
        generator = templates.get(backend)
        if generator:
            return generator(api_name, industry)
        
        return f"// {api_name} API template for {backend}"
    
    def _nextjs_page_template(self, page_name: str, industry: str) -> str:
        """Generate Next.js page template"""
        component_name = ''.join(word.capitalize() for word in page_name.split('_'))
        
        return f"""'use client';

import React from 'react';
import {{ useState, useEffect }} from 'react';
import {{ useRouter }} from 'next/navigation';

interface {component_name}PageProps {{
  // Add props here
}}

export default function {component_name}Page({{}}: {component_name}PageProps) {{
  const router = useRouter();
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState(null);

  useEffect(() => {{
    // Fetch data on mount
    fetchData();
  }}, []);

  const fetchData = async () => {{
    setLoading(true);
    try {{
      // Add API call here
      const response = await fetch('/api/{page_name}');
      const result = await response.json();
      setData(result);
    }} catch (error) {{
      console.error('Error fetching data:', error);
    }} finally {{
      setLoading(false);
    }}
  }};

  if (loading) {{
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary"></div>
      </div>
    );
  }}

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-6">{component_name}</h1>
      
      {{/* Add your page content here */}}
      <div className="grid gap-6">
        {{/* Industry-specific content for {industry} */}}
      </div>
    </div>
  );
}}"""
    
    def _nuxt_page_template(self, page_name: str, industry: str) -> str:
        """Generate Nuxt page template"""
        component_name = ''.join(word.capitalize() for word in page_name.split('_'))
        
        return f"""<template>
  <div class="container mx-auto px-4 py-8">
    <h1 class="text-3xl font-bold mb-6">{component_name}</h1>
    
    <div v-if="pending" class="flex items-center justify-center">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-primary"></div>
    </div>
    
    <div v-else class="grid gap-6">
      <!-- Industry-specific content for {industry} -->
    </div>
  </div>
</template>

<script setup lang="ts">
import {{ ref, onMounted }} from 'vue'

// Define reactive data
const pending = ref(false)
const data = ref(null)

// Fetch data function
const fetchData = async () => {{
  pending.value = true
  try {{
    const response = await $fetch('/api/{page_name}')
    data.value = response
  }} catch (error) {{
    console.error('Error fetching data:', error)
  }} finally {{
    pending.value = false
  }}
}}

// Lifecycle
onMounted(() => {{
  fetchData()
}})
</script>

<style scoped>
/* Add component-specific styles here */
</style>"""
    
    def _angular_page_template(self, page_name: str, industry: str) -> str:
        """Generate Angular component template"""
        component_name = ''.join(word.capitalize() for word in page_name.split('_'))
        
        return f"""import {{ Component, OnInit }} from '@angular/core';
import {{ Observable }} from 'rxjs';
import {{ HttpClient }} from '@angular/common/http';

@Component({{
  selector: 'app-{page_name.replace('_', '-')}',
  templateUrl: './{page_name}.component.html',
  styleUrls: ['./{page_name}.component.scss']
}})
export class {component_name}Component implements OnInit {{
  loading = false;
  data: any = null;
  error: string | null = null;

  constructor(private http: HttpClient) {{ }}

  ngOnInit(): void {{
    this.loadData();
  }}

  loadData(): void {{
    this.loading = true;
    this.http.get(`/api/{page_name}`).subscribe({{
      next: (response) => {{
        this.data = response;
        this.loading = false;
      }},
      error: (error) => {{
        this.error = 'Failed to load data';
        this.loading = false;
        console.error('Error:', error);
      }}
    }});
  }}
}}"""
    
    def _expo_page_template(self, page_name: str, industry: str) -> str:
        """Generate Expo screen template"""
        component_name = ''.join(word.capitalize() for word in page_name.split('_'))
        
        return f"""import React, {{ useState, useEffect }} from 'react';
import {{
  View,
  Text,
  ScrollView,
  ActivityIndicator,
  StyleSheet,
  RefreshControl,
}} from 'react-native';
import {{ SafeAreaView }} from 'react-native-safe-area-context';
import {{ useNavigation }} from '@react-navigation/native';

export default function {component_name}Screen() {{
  const navigation = useNavigation();
  const [loading, setLoading] = useState(false);
  const [refreshing, setRefreshing] = useState(false);
  const [data, setData] = useState(null);

  useEffect(() => {{
    fetchData();
  }}, []);

  const fetchData = async () => {{
    setLoading(true);
    try {{
      // Add API call here
      const response = await fetch('https://api.example.com/{page_name}');
      const result = await response.json();
      setData(result);
    }} catch (error) {{
      console.error('Error fetching data:', error);
    }} finally {{
      setLoading(false);
      setRefreshing(false);
    }}
  }};

  const onRefresh = () => {{
    setRefreshing(true);
    fetchData();
  }};

  if (loading && !refreshing) {{
    return (
      <SafeAreaView style={styles.container}>
        <ActivityIndicator size="large" color="#0000ff" />
      </SafeAreaView>
    );
  }}

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView
        contentContainerStyle={styles.scrollContent}
        refreshControl={{
          <RefreshControl refreshing={{refreshing}} onRefresh={{onRefresh}} />
        }}
      >
        <Text style={styles.title}>{component_name}</Text>
        
        {{/* Industry-specific content for {industry} */}}
        
      </ScrollView>
    </SafeAreaView>
  );
}}

const styles = StyleSheet.create({{
  container: {{
    flex: 1,
    backgroundColor: '#fff',
  }},
  scrollContent: {{
    padding: 16,
  }},
  title: {{
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 16,
  }},
}});"""
    
    def _fastapi_api_template(self, api_name: str, industry: str) -> str:
        """Generate FastAPI endpoint template"""
        router_name = api_name.replace('_api', '')
        # Precompute industry-specific suffix to avoid f-string expressions with backslashes
        extra_lines: list[str] = []
        if industry == "healthcare":
            extra_lines.append("# Add HIPAA-compliant audit logging")
        if industry == "finance":
            extra_lines.append("# Add financial transaction validation")
        if industry == "ecommerce":
            extra_lines.append("# Add inventory management integration")
        industry_suffix = "\n".join(extra_lines)

        return f"""from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
import logging

from app.database import get_db
from app.models import {router_name.capitalize()}Model
from app.schemas import {router_name.capitalize()}Create, {router_name.capitalize()}Update, {router_name.capitalize()}Response
from app.auth import get_current_user

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/{router_name}s", tags=["{router_name}s"])

@router.get("/", response_model=List[{router_name.capitalize()}Response])
async def list_{router_name}s(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    \"\"\"
    List all {router_name}s with pagination
    \"\"\"
    try:
        items = db.query({router_name.capitalize()}Model).offset(skip).limit(limit).all()
        return items
    except Exception as e:
        logger.error(f"Error listing {router_name}s: {{str(e)}}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/{{{router_name}_id}}", response_model={router_name.capitalize()}Response)
async def get_{router_name}(
    {router_name}_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    \"\"\"
    Get a specific {router_name} by ID
    \"\"\"
    item = db.query({router_name.capitalize()}Model).filter(
        {router_name.capitalize()}Model.id == {router_name}_id
    ).first()
    
    if not item:
        raise HTTPException(status_code=404, detail="{router_name.capitalize()} not found")
    
    return item

@router.post("/", response_model={router_name.capitalize()}Response, status_code=201)
async def create_{router_name}(
    {router_name}: {router_name.capitalize()}Create,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    \"\"\"
    Create a new {router_name}
    \"\"\"
    try:
        db_item = {router_name.capitalize()}Model(
            **{router_name}.dict(),
            created_by=current_user.id,
            created_at=datetime.utcnow()
        )
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        
        logger.info(f"{router_name.capitalize()} created with ID: {{db_item.id}}")
        return db_item
    except Exception as e:
        logger.error(f"Error creating {router_name}: {{str(e)}}")
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{{{router_name}_id}}", response_model={router_name.capitalize()}Response)
async def update_{router_name}(
    {router_name}_id: int,
    {router_name}: {router_name.capitalize()}Update,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    \"\"\"
    Update an existing {router_name}
    \"\"\"
    db_item = db.query({router_name.capitalize()}Model).filter(
        {router_name.capitalize()}Model.id == {router_name}_id
    ).first()
    
    if not db_item:
        raise HTTPException(status_code=404, detail="{router_name.capitalize()} not found")
    
    try:
        update_data = {router_name}.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_item, field, value)
        
        db_item.updated_at = datetime.utcnow()
        db_item.updated_by = current_user.id
        
        db.commit()
        db.refresh(db_item)
        
        logger.info(f"{router_name.capitalize()} updated with ID: {{db_item.id}}")
        return db_item
    except Exception as e:
        logger.error(f"Error updating {router_name}: {{str(e)}}")
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{{{router_name}_id}}", status_code=204)
async def delete_{router_name}(
    {router_name}_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    \"\"\"
    Delete a {router_name}
    \"\"\"
    db_item = db.query({router_name.capitalize()}Model).filter(
        {router_name.capitalize()}Model.id == {router_name}_id
    ).first()
    
    if not db_item:
        raise HTTPException(status_code=404, detail="{router_name.capitalize()} not found")
    
    try:
        db.delete(db_item)
        db.commit()
        
        logger.info(f"{router_name.capitalize()} deleted with ID: {{{router_name}_id}}")
        return None
    except Exception as e:
        logger.error(f"Error deleting {router_name}: {{str(e)}}")
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

# Industry-specific endpoints for {industry}
{industry_suffix}
"""
    
    def _django_api_template(self, api_name: str, industry: str) -> str:
        """Generate Django REST API template"""
        model_name = api_name.replace('_api', '').capitalize()
        # Precompute industry-specific suffix
        django_lines: list[str] = []
        if industry == "healthcare":
            django_lines.append("""@action(detail=True, methods=['post'])
    def audit_log(self, request, pk=None):
        '''Add audit log entry (HIPAA compliance)'''
        pass""")
        if industry == "finance":
            django_lines.append("""@action(detail=True, methods=['post'])
    def validate_transaction(self, request, pk=None):
        '''Validate financial transaction'''
        pass""")
        if industry == "ecommerce":
            django_lines.append("""@action(detail=True, methods=['get'])
    def inventory_status(self, request, pk=None):
        '''Check inventory status'''
        pass""")
        django_suffix = "\n".join(django_lines)

        return f"""from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction
from django.utils import timezone
import logging

from .models import {model_name}
from .serializers import {model_name}Serializer, {model_name}CreateSerializer, {model_name}UpdateSerializer
from .permissions import IsOwnerOrReadOnly
from .filters import {model_name}Filter

logger = logging.getLogger(__name__)

class {model_name}ViewSet(viewsets.ModelViewSet):
    \"\"\"
    ViewSet for {model_name} operations
    \"\"\"
    queryset = {model_name}.objects.all()
    serializer_class = {model_name}Serializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = {model_name}Filter
    ordering_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
    
    def get_serializer_class(self):
        if self.action == 'create':
            return {model_name}CreateSerializer
        elif self.action in ['update', 'partial_update']:
            return {model_name}UpdateSerializer
        return {model_name}Serializer
    
    def perform_create(self, serializer):
        \"\"\"Create a new {model_name.lower()}\"\"\"
        try:
            with transaction.atomic():
                serializer.save(
                    created_by=self.request.user,
                    created_at=timezone.now()
                )
                logger.info(f"{model_name} created by user {{self.request.user.id}}")
        except Exception as e:
            logger.error(f"Error creating {model_name}: {{str(e)}}")
            raise
    
    def perform_update(self, serializer):
        \"\"\"Update an existing {model_name.lower()}\"\"\"
        try:
            with transaction.atomic():
                serializer.save(
                    updated_by=self.request.user,
                    updated_at=timezone.now()
                )
                logger.info(f"{model_name} {{serializer.instance.id}} updated by user {{self.request.user.id}}")
        except Exception as e:
            logger.error(f"Error updating {model_name}: {{str(e)}}")
            raise
    
    def destroy(self, request, *args, **kwargs):
        \"\"\"Delete a {model_name.lower()}\"\"\"
        instance = self.get_object()
        try:
            with transaction.atomic():
                instance.delete()
                logger.info(f"{model_name} {{instance.id}} deleted by user {{request.user.id}}")
                return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logger.error(f"Error deleting {model_name}: {{str(e)}}")
            return Response(
                {{'error': 'Failed to delete resource'}},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    @action(detail=False, methods=['get'])
    def stats(self, request):
        \"\"\"Get statistics for {model_name.lower()}s\"\"\"
        total = self.get_queryset().count()
        recent = self.get_queryset().filter(
            created_at__gte=timezone.now() - timezone.timedelta(days=30)
        ).count()
        
        return Response({{
            'total': total,
            'recent': recent,
            'by_user': request.user.{model_name.lower()}_set.count()
        }})
    
    # Industry-specific methods for {industry}
    {django_suffix}
"""
    
    def _nestjs_api_template(self, api_name: str, industry: str) -> str:
        """Generate NestJS controller template"""
        entity_name = ''.join(word.capitalize() for word in api_name.replace('_api', '').split('_'))
        # Precompute industry-specific suffix
        nest_lines: list[str] = []
        if industry == "healthcare":
            nest_lines.append("""@Post(':id/audit')
  @ApiOperation({ summary: 'Add audit log entry (HIPAA compliance)' })
  async addAuditLog(@Param('id') id: string, @Body() auditData: any, @CurrentUser() user: User) {
    // Implementation for HIPAA audit logging
  }""")
        if industry == "finance":
            nest_lines.append("""@Post(':id/validate-transaction')
  @ApiOperation({ summary: 'Validate financial transaction' })
  async validateTransaction(@Param('id') id: string, @Body() transactionData: any, @CurrentUser() user: User) {
    // Implementation for financial validation
  }""")
        if industry == "ecommerce":
            nest_lines.append("""@Get(':id/inventory')
  @ApiOperation({ summary: 'Check inventory status' })
  async checkInventory(@Param('id') id: string, @CurrentUser() user: User) {
    // Implementation for inventory check
  }""")
        nest_suffix = "\n".join(nest_lines)

        return f"""import {{
  Controller,
  Get,
  Post,
  Put,
  Delete,
  Body,
  Param,
  Query,
  UseGuards,
  Logger,
  HttpException,
  HttpStatus,
}} from '@nestjs/common';
import {{ ApiTags, ApiOperation, ApiResponse, ApiBearerAuth }} from '@nestjs/swagger';
import {{ JwtAuthGuard }} from '../auth/jwt-auth.guard';
import {{ {entity_name}Service }} from './{api_name.replace('_api', '')}.service';
import {{ Create{entity_name}Dto }} from './dto/create-{api_name.replace('_api', '')}.dto';
import {{ Update{entity_name}Dto }} from './dto/update-{api_name.replace('_api', '')}.dto';
import {{ {entity_name} }} from './entities/{api_name.replace('_api', '')}.entity';
import {{ CurrentUser }} from '../auth/current-user.decorator';
import {{ User }} from '../users/entities/user.entity';

@ApiTags('{api_name.replace('_api', '')}s')
@ApiBearerAuth()
@UseGuards(JwtAuthGuard)
@Controller('{api_name.replace('_api', '')}s')
export class {entity_name}Controller {{
  private readonly logger = new Logger({entity_name}Controller.name);

  constructor(private readonly {entity_name.lower()}Service: {entity_name}Service) {{}}

  @Get()
  @ApiOperation({{ summary: 'List all {api_name.replace('_api', '')}s' }})
  @ApiResponse({{ status: 200, description: 'Return all {api_name.replace('_api', '')}s' }})
  async findAll(
    @Query('skip') skip = 0,
    @Query('take') take = 100,
    @CurrentUser() user: User,
  ): Promise<{entity_name}[]> {{
    try {{
      this.logger.log(`User ${{user.id}} listing {api_name.replace('_api', '')}s`);
      return await this.{entity_name.lower()}Service.findAll({{ skip, take }});
    }} catch (error) {{
      this.logger.error(`Error listing {api_name.replace('_api', '')}s: ${{error.message}}`);
      throw new HttpException('Internal server error', HttpStatus.INTERNAL_SERVER_ERROR);
    }}
  }}

  @Get(':id')
  @ApiOperation({{ summary: 'Get a {api_name.replace('_api', '')} by id' }})
  @ApiResponse({{ status: 200, description: 'Return the {api_name.replace('_api', '')}' }})
  @ApiResponse({{ status: 404, description: '{entity_name} not found' }})
  async findOne(
    @Param('id') id: string,
    @CurrentUser() user: User,
  ): Promise<{entity_name}> {{
    const result = await this.{entity_name.lower()}Service.findOne(+id);
    if (!result) {{
      throw new HttpException('{entity_name} not found', HttpStatus.NOT_FOUND);
    }}
    return result;
  }}

  @Post()
  @ApiOperation({{ summary: 'Create a new {api_name.replace('_api', '')}' }})
  @ApiResponse({{ status: 201, description: '{entity_name} created successfully' }})
  @ApiResponse({{ status: 400, description: 'Bad request' }})
  async create(
    @Body() create{entity_name}Dto: Create{entity_name}Dto,
    @CurrentUser() user: User,
  ): Promise<{entity_name}> {{
    try {{
      const result = await this.{entity_name.lower()}Service.create({{
        ...create{entity_name}Dto,
        createdBy: user.id,
        createdAt: new Date(),
      }});
      this.logger.log(`{entity_name} created with ID: ${{result.id}} by user ${{user.id}}`);
      return result;
    }} catch (error) {{
      this.logger.error(`Error creating {api_name.replace('_api', '')}: ${{error.message}}`);
      throw new HttpException(error.message, HttpStatus.BAD_REQUEST);
    }}
  }}

  @Put(':id')
  @ApiOperation({{ summary: 'Update a {api_name.replace('_api', '')}' }})
  @ApiResponse({{ status: 200, description: '{entity_name} updated successfully' }})
  @ApiResponse({{ status: 404, description: '{entity_name} not found' }})
  async update(
    @Param('id') id: string,
    @Body() update{entity_name}Dto: Update{entity_name}Dto,
    @CurrentUser() user: User,
  ): Promise<{entity_name}> {{
    try {{
      const result = await this.{entity_name.lower()}Service.update(+id, {{
        ...update{entity_name}Dto,
        updatedBy: user.id,
        updatedAt: new Date(),
      }});
      if (!result) {{
        throw new HttpException('{entity_name} not found', HttpStatus.NOT_FOUND);
      }}
      this.logger.log(`{entity_name} ${{id}} updated by user ${{user.id}}`);
      return result;
    }} catch (error) {{
      this.logger.error(`Error updating {api_name.replace('_api', '')}: ${{error.message}}`);
      if (error instanceof HttpException) {{
        throw error;
      }}
      throw new HttpException(error.message, HttpStatus.BAD_REQUEST);
    }}
  }}

  @Delete(':id')
  @ApiOperation({{ summary: 'Delete a {api_name.replace('_api', '')}' }})
  @ApiResponse({{ status: 204, description: '{entity_name} deleted successfully' }})
  @ApiResponse({{ status: 404, description: '{entity_name} not found' }})
  async remove(
    @Param('id') id: string,
    @CurrentUser() user: User,
  ): Promise<void> {{
    try {{
      const result = await this.{entity_name.lower()}Service.remove(+id);
      if (!result) {{
        throw new HttpException('{entity_name} not found', HttpStatus.NOT_FOUND);
      }}
      this.logger.log(`{entity_name} ${{id}} deleted by user ${{user.id}}`);
    }} catch (error) {{
      this.logger.error(`Error deleting {api_name.replace('_api', '')}: ${{error.message}}`);
      if (error instanceof HttpException) {{
        throw error;
      }}
      throw new HttpException(error.message, HttpStatus.BAD_REQUEST);
    }}
  }}

  // Industry-specific endpoints for {industry}
  {nest_suffix}
}}"""
    
    def _go_api_template(self, api_name: str, industry: str) -> str:
        """Generate Go API handler template"""
        entity_name = ''.join(word.capitalize() for word in api_name.replace('_api', '').split('_'))
        # Precompute industry-specific suffix
        go_lines: list[str] = []
        if industry == "healthcare":
            go_lines.append("""// AddAuditLog handles HIPAA-compliant audit logging
func (h *{entity_name}Handler) AddAuditLog(w http.ResponseWriter, r *http.Request) {
    // Implementation for HIPAA audit logging
}""")
        if industry == "finance":
            go_lines.append("""// ValidateTransaction handles financial transaction validation
func (h *{entity_name}Handler) ValidateTransaction(w http.ResponseWriter, r *http.Request) {
    // Implementation for financial validation
}""")
        if industry == "ecommerce":
            go_lines.append("""// CheckInventory handles inventory status checks
func (h *{entity_name}Handler) CheckInventory(w http.ResponseWriter, r *http.Request) {
    // Implementation for inventory check
}""")
        go_suffix = "\n".join(go_lines)

        return f"""package handlers

import (
    "encoding/json"
    "net/http"
    "strconv"
    "time"
    
    "github.com/gorilla/mux"
    "github.com/sirupsen/logrus"
    
    "myapp/models"
    "myapp/services"
    "myapp/middleware"
)

type {entity_name}Handler struct {{
    service *services.{entity_name}Service
    logger  *logrus.Logger
}}

func New{entity_name}Handler(service *services.{entity_name}Service, logger *logrus.Logger) *{entity_name}Handler {{
    return &{entity_name}Handler{{
        service: service,
        logger:  logger,
    }}
}}

// List{entity_name}s godoc
// @Summary List all {api_name.replace('_api', '')}s
// @Description Get a list of all {api_name.replace('_api', '')}s with pagination
// @Tags {api_name.replace('_api', '')}s
// @Accept json
// @Produce json
// @Param skip query int false "Skip records"
// @Param limit query int false "Limit records"
// @Success 200 {{array}} models.{entity_name}
// @Failure 500 {{object}} models.ErrorResponse
// @Router /{api_name.replace('_api', '')}s [get]
func (h *{entity_name}Handler) List{entity_name}s(w http.ResponseWriter, r *http.Request) {{
    skip, _ := strconv.Atoi(r.URL.Query().Get("skip"))
    limit, _ := strconv.Atoi(r.URL.Query().Get("limit"))
    if limit == 0 || limit > 100 {{
        limit = 100
    }}
    
    userID := middleware.GetUserID(r.Context())
    h.logger.WithField("user_id", userID).Info("Listing {api_name.replace('_api', '')}s")
    
    items, err := h.service.List(skip, limit)
    if err != nil {{
        h.logger.WithError(err).Error("Failed to list {api_name.replace('_api', '')}s")
        respondWithError(w, http.StatusInternalServerError, "Internal server error")
        return
    }}
    
    respondWithJSON(w, http.StatusOK, items)
}}

// Get{entity_name} godoc
// @Summary Get a {api_name.replace('_api', '')}
// @Description Get a {api_name.replace('_api', '')} by ID
// @Tags {api_name.replace('_api', '')}s
// @Accept json
// @Produce json
// @Param id path int true "{entity_name} ID"
// @Success 200 {{object}} models.{entity_name}
// @Failure 404 {{object}} models.ErrorResponse
// @Failure 500 {{object}} models.ErrorResponse
// @Router /{api_name.replace('_api', '')}s/{{id}} [get]
func (h *{entity_name}Handler) Get{entity_name}(w http.ResponseWriter, r *http.Request) {{
    vars := mux.Vars(r)
    id, err := strconv.Atoi(vars["id"])
    if err != nil {{
        respondWithError(w, http.StatusBadRequest, "Invalid ID")
        return
    }}
    
    item, err := h.service.GetByID(id)
    if err != nil {{
        if err == services.ErrNotFound {{
            respondWithError(w, http.StatusNotFound, "{entity_name} not found")
            return
        }}
        h.logger.WithError(err).Error("Failed to get {api_name.replace('_api', '')}")
        respondWithError(w, http.StatusInternalServerError, "Internal server error")
        return
    }}
    
    respondWithJSON(w, http.StatusOK, item)
}}

// Create{entity_name} godoc
// @Summary Create a {api_name.replace('_api', '')}
// @Description Create a new {api_name.replace('_api', '')}
// @Tags {api_name.replace('_api', '')}s
// @Accept json
// @Produce json
// @Param {api_name.replace('_api', '')} body models.{entity_name}Create true "{entity_name} object"
// @Success 201 {{object}} models.{entity_name}
// @Failure 400 {{object}} models.ErrorResponse
// @Failure 500 {{object}} models.ErrorResponse
// @Router /{api_name.replace('_api', '')}s [post]
func (h *{entity_name}Handler) Create{entity_name}(w http.ResponseWriter, r *http.Request) {{
    var input models.{entity_name}Create
    if err := json.NewDecoder(r.Body).Decode(&input); err != nil {{
        respondWithError(w, http.StatusBadRequest, "Invalid request payload")
        return
    }}
    
    userID := middleware.GetUserID(r.Context())
    input.CreatedBy = userID
    input.CreatedAt = time.Now()
    
    item, err := h.service.Create(&input)
    if err != nil {{
        h.logger.WithError(err).Error("Failed to create {api_name.replace('_api', '')}")
        respondWithError(w, http.StatusBadRequest, err.Error())
        return
    }}
    
    h.logger.WithFields(logrus.Fields{{
        "id":      item.ID,
        "user_id": userID,
    }}).Info("{entity_name} created")
    
    respondWithJSON(w, http.StatusCreated, item)
}}

// Update{entity_name} godoc
// @Summary Update a {api_name.replace('_api', '')}
// @Description Update an existing {api_name.replace('_api', '')}
// @Tags {api_name.replace('_api', '')}s
// @Accept json
// @Produce json
// @Param id path int true "{entity_name} ID"
// @Param {api_name.replace('_api', '')} body models.{entity_name}Update true "{entity_name} object"
// @Success 200 {{object}} models.{entity_name}
// @Failure 400 {{object}} models.ErrorResponse
// @Failure 404 {{object}} models.ErrorResponse
// @Failure 500 {{object}} models.ErrorResponse
// @Router /{api_name.replace('_api', '')}s/{{id}} [put]
func (h *{entity_name}Handler) Update{entity_name}(w http.ResponseWriter, r *http.Request) {{
    vars := mux.Vars(r)
    id, err := strconv.Atoi(vars["id"])
    if err != nil {{
        respondWithError(w, http.StatusBadRequest, "Invalid ID")
        return
    }}
    
    var input models.{entity_name}Update
    if err := json.NewDecoder(r.Body).Decode(&input); err != nil {{
        respondWithError(w, http.StatusBadRequest, "Invalid request payload")
        return
    }}
    
    userID := middleware.GetUserID(r.Context())
    input.UpdatedBy = userID
    input.UpdatedAt = time.Now()
    
    item, err := h.service.Update(id, &input)
    if err != nil {{
        if err == services.ErrNotFound {{
            respondWithError(w, http.StatusNotFound, "{entity_name} not found")
            return
        }}
        h.logger.WithError(err).Error("Failed to update {api_name.replace('_api', '')}")
        respondWithError(w, http.StatusBadRequest, err.Error())
        return
    }}
    
    h.logger.WithFields(logrus.Fields{{
        "id":      id,
        "user_id": userID,
    }}).Info("{entity_name} updated")
    
    respondWithJSON(w, http.StatusOK, item)
}}

// Delete{entity_name} godoc
// @Summary Delete a {api_name.replace('_api', '')}
// @Description Delete a {api_name.replace('_api', '')}
// @Tags {api_name.replace('_api', '')}s
// @Accept json
// @Produce json
// @Param id path int true "{entity_name} ID"
// @Success 204 "No Content"
// @Failure 404 {{object}} models.ErrorResponse
// @Failure 500 {{object}} models.ErrorResponse
// @Router /{api_name.replace('_api', '')}s/{{id}} [delete]
func (h *{entity_name}Handler) Delete{entity_name}(w http.ResponseWriter, r *http.Request) {{
    vars := mux.Vars(r)
    id, err := strconv.Atoi(vars["id"])
    if err != nil {{
        respondWithError(w, http.StatusBadRequest, "Invalid ID")
        return
    }}
    
    userID := middleware.GetUserID(r.Context())
    
    if err := h.service.Delete(id); err != nil {{
        if err == services.ErrNotFound {{
            respondWithError(w, http.StatusNotFound, "{entity_name} not found")
            return
        }}
        h.logger.WithError(err).Error("Failed to delete {api_name.replace('_api', '')}")
        respondWithError(w, http.StatusBadRequest, err.Error())
        return
    }}
    
    h.logger.WithFields(logrus.Fields{{
        "id":      id,
        "user_id": userID,
    }}).Info("{entity_name} deleted")
    
    w.WriteHeader(http.StatusNoContent)
}}

// Industry-specific handlers for {industry}
{go_suffix}

// Helper functions
func respondWithError(w http.ResponseWriter, code int, message string) {{
    respondWithJSON(w, code, map[string]string{{"error": message}})
}}

func respondWithJSON(w http.ResponseWriter, code int, payload interface{{}}) {{
    response, _ := json.Marshal(payload)
    w.Header().Set("Content-Type", "application/json")
    w.WriteHeader(code)
    w.Write(response)
}}
}}"""